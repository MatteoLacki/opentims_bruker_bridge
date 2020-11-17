all:
	pip uninstall opentims_bruker_bridge -y
	pip install . --user
make:
	echo "hello"
upload_test_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine -r testpypi dist/* 
upload_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine upload dist/*
py:
	python -m IPython
