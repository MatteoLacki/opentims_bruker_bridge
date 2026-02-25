all:
	pip uninstall opentims_bruker_bridge -y
	pip install . --user
make:
	echo "hello"
sdist:
	python -m build --sdist

upload_test_pypi: sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*  --verbose

upload_pypi: sdist
	python setup.py sdist
	twine upload dist/* --verbose

clean:
	rm -rf dist
py:
	python -m IPython
clean:
	rm -rf dist build *.egg-info
