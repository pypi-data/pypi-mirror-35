all:
	# PySpark only knows eggs, not wheels
	python setup.py sdist

upload:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

test:
	python setup.py develop
	python setup.py test
	flake8 --max-line-length=120 taar_lite tests
