from setuptools import find_packages, setup

setup(
    name='mozilla-taarlite',
    use_scm_version=False,
    version='0.3.0-pre1',
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests/*']),
    description='Telemetry-Aware Addon Recommender Lite',
    author='Mozilla Foundation',
    author_email='fx-data-dev@mozilla.org',
    url='https://github.com/mozilla/taar-lite',
    license='MPL 2.0',
    install_requires=[
        'mozilla-srgutil',
        'numpy',
        'requests',
        'six',
        'boto3',
        'scipy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    zip_safe=False,
)
