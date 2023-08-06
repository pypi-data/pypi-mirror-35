all: clean
	python ./setup.py sdist bdist_wheel
	#pip install --upgrade dist/ReSubuser-0.0.10-py3-none-any.whl --user -v
	twine upload dist/*

clean:
	rm dist build *.egg-info -rf

