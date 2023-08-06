all: clean
	python ./setup.py sdist bdist_wheel
	pip install --upgrade dist/ReSubuser-*.whl --user -v

clean:
	rm dist build *.egg-info -rf

upload:
	twine upload dist/*
