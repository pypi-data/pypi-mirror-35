# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

"""Provides a GuidBasedRecommender for use in production

Adds in the S3 context with the help of the srgutil Context.
"""

import numpy as np

from decouple import config
from srgutil.interfaces import IS3Data, IMozLogging
from .utils.cache import LazyJSONLoader
from .recommenders.guidguid import GuidGuidCoinstallRecommender
from .recommenders.treatments import (
    Guidception,
    NoTreatment,
    RowCount,
    RowNormSum,
    RowSum
)

ADDON_LIST_BUCKET = 'telemetry-parquet'
ADDON_LIST_KEY = 'taar/lite/guid_coinstallation.json'
GUID_RANKING_KEY = 'taar/lite/guid_install_ranking.json'

ADDON_DL_ERR = "Cannot download addon coinstallation file {}".format(ADDON_LIST_KEY)   # noqa
TAAR_CACHE_EXPIRY = config('TAAR_CACHE_EXPIRY', default=14400, cast=int)

NORM_MODE_ROWNORMSUM = 'rownorm_sum'
NORM_MODE_ROWCOUNT = 'row_count'
NORM_MODE_ROWSUM = 'row_sum'
NORM_MODE_GUIDCEPTION = 'guidception'

# TODO BirdNote - Delete before merging
# This only required modest changes to use the new
# Recommender and Treatment classes. The main difference is that there's
# no norm_dict instead there's the _recommenders dict which gets rebuilt
# whenever json is reloaded and then that is used directly to pull recommendations


class GuidBasedRecommender:
    """ A recommender class that returns top N addons based on a
    passed addon identifier.  This will load a json file containing
    updated top n addons coinstalled with the addon passed as an input
    parameter based on periodically updated  addon-addon
    coinstallation frequency table generated from  Longitdudinal
    Telemetry data.  This recommender will drive recommendations
    surfaced on addons.mozilla.org
    """

    _addons_coinstallations = None
    _recommenders = {}

    # Define recursion levels for guid-ception
    RECURSION_LEVELS = 3

    def __init__(self, ctx):
        self._ctx = ctx
        assert IS3Data in self._ctx

        if 'coinstall_loader' in self._ctx:
            self._addons_coinstall_loader = self._ctx['coinstall_loader']
        else:
            self._addons_coinstall_loader = LazyJSONLoader(self._ctx,
                                                           ADDON_LIST_BUCKET,
                                                           ADDON_LIST_KEY,
                                                           TAAR_CACHE_EXPIRY)

        if 'ranking_loader' in self._ctx:
            self._guid_ranking_loader = self._ctx['ranking_loader']
        else:
            self._guid_ranking_loader = LazyJSONLoader(self._ctx,
                                                       ADDON_LIST_BUCKET,
                                                       GUID_RANKING_KEY,
                                                       TAAR_CACHE_EXPIRY)

        self._init_from_ctx()

        # Force access to the JSON models for each request at
        # recommender construction.  This was lifted out of the
        # constructor for the LazyJSONLoader so that the
        # precomputation of the normalization tables can be done in
        # the recommender.
        _ = self._addons_coinstallations  # noqa
        _ = self._guid_rankings           # noqa

        self.logger.info("GUIDBasedRecommender is initialized")

    def _init_from_ctx(self):
        self.logger = self._ctx[IMozLogging].get_logger('taarlite')

        if self._addons_coinstallations is None:
            self.logger.error(ADDON_DL_ERR)

        # Compute the floor install incidence that recommended addons
        # must satisfy.  Take 5% of the mean of all installed addons.
        self._min_installs = np.mean(list(self._guid_rankings.values())) * 0.05

        # Warn if the minimum number of installs drops below 100.
        if self._min_installs < 100:
            self.logger.warn("minimum installs threshold low: [%s]" % self._min_installs)

    @property
    def _addons_coinstallations(self):
        result, refreshed = self._addons_coinstall_loader.get()
        if refreshed:
            self.logger.info("Refreshing guid_maps for normalization")
            self._precompute_recommenders()
        return result

    @property
    def _guid_rankings(self):
        result, refreshed = self._guid_ranking_loader.get()
        if refreshed:
            self.logger.info("Refreshing guid_maps for normalization")
            self._precompute_recommenders()
        return result

    def _precompute_recommenders(self):
        def get_recommender(treatment):
            return GuidGuidCoinstallRecommender(
                self._addons_coinstallations,
                self._guid_rankings,
                treatment,
                validate_raw_coinstallation_graph=False
            )
        self._recommenders = {
            'none': get_recommender(NoTreatment()),
            NORM_MODE_ROWCOUNT: get_recommender(RowCount()),
            NORM_MODE_ROWSUM: get_recommender(RowSum()),
            NORM_MODE_ROWNORMSUM: get_recommender(RowNormSum()),
            NORM_MODE_GUIDCEPTION: get_recommender(Guidception()),
        }

    def recommend(self, client_data, limit=4):
        """
        TAAR lite will yield 4 recommendations for the AMO page
        """

        # Force access to the JSON models for each request at the
        # start of the request to update normalization tables if
        # required.
        _ = self._addons_coinstallations  # noqa
        _ = self._guid_rankings           # noqa

        addon_guid = client_data.get('guid')
        normalize = client_data.get('normalize', NORM_MODE_ROWNORMSUM)

        if normalize is not None and normalize not in self._recommenders:
            # Yield no results if the normalization method is not specified
            self.logger.warn("Invalid normalization parameter detected: [%s]" % normalize)
            return []

        result_list = self._recommenders[normalize].recommend(addon_guid, limit)

        log_data = (str(addon_guid), [str(r) for r in result_list])
        self.logger.info("Addon: [%s] triggered these recommendation guids: [%s]" % log_data)

        return result_list

    def can_recommend(self, client_data):
        # TODO - I can't see anywhere this is used.

        # We can't recommend if we don't have our data files.
        if self._addons_coinstallations is None:
            return False

        # If we have data coming from other sources, we can use that for
        # recommending.
        addon_guid = client_data.get('guid', None)
        if not isinstance(addon_guid, str):
            return False

        # Use a dictionary keyed on the query guid
        if addon_guid not in self._addons_coinstallations.keys():
            return False

        if not self._addons_coinstallations.get(addon_guid):
            return False

        return True
