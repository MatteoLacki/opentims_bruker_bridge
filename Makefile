all:
	pip uninstall opentims_bruker_bridge -y
	pip install . --user
make:
	echo "hello"
sdist:
	python setup.py sdist
upload_test_pypi: sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
upload_pypi: sdist
	twine upload dist/*
clean:
	rm -rf dist
py:
	python -m IPython
