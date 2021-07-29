all:
	pip uninstall opentims_bruker_bridge -y
	pip install . --user
make:
	echo "hello"
upload_test_pypi: clean
	python setup.py sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
upload_pypi: clean
	python setup.py sdist
	twine upload dist/*
py:
	python -m IPython
clean:
	rm -rf dist build *.egg-info
