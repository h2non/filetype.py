all: lint unit

export PYTHONPATH:=${PWD}
version=`python -c 'import filetype; print(filetype.version)'`
filename=filetype-`python -c 'import filetype;print(filetype.version)'`.tar.gz

lint:
	@flake8 .

test: clean lint
	@echo "Running tests ..."
	@python -m unittest discover

documentation:
	@pdoc --html --overwrite --all-submodules --html-dir docs filetype
	@rm -rf docs/v${version}
	@mv docs/filetype docs/v${version}

deploy-documentation: documentation
	@cd docs && git checkout gh-pages
	@cd docs && git add .
	@cd docs && git commit -am release
	@cd docs && git push --force origin gh-pages

clean:
	@printf "Cleaning up files that are already in .gitignore... "
	@for pattern in `cat .gitignore`; do find . -name "$$pattern" -delete; done
	@echo "OK!"

tag:
	@echo "Creating tag v$(version)..."
	@echo $(version)
	@git tag -a v$(version) -m "Version v$(version)"
	@git push origin v$(version)

compress:
	@printf "Exporting to $(filename)... "
	@tar czf $(filename) filetype setup.py README.md LICENSE

publish:
	@echo "==> Releasing package $(version)..."
	@python setup.py sdist bdist_wheel
	@twine upload dist/* --repository-url https://upload.pypi.org/legacy/
	@rm -fr build dist .egg pook.egg-info

release: clean docs deploy-documentation tag compress publish
	@echo "DONE!"
