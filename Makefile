all: check_dependencies unit functional doctest

filename=filetype-`python -c 'import filetype;print filetype.version'`.tar.gz

check_dependencies:
	@echo "Checking for dependencies to run tests ..."
	@for dependency in `echo $$LETTUCE_DEPENDENCIES`; do \
		python -c "import $$dependency" 2>/dev/null || (echo "You must install $$dependency in order to run filetype's tests" && exit 3) ; \
		done

unit: clean lint
	@echo "Running unit tests ..."
	@nosetests -s --verbosity=2 --with-coverage --cover-erase --cover-inclusive tests/unit --cover-package=filetype

doctest: clean
	@cd docs && make doctest

documentation:
	@cd docs && make html

clean:
	@printf "Cleaning up files that are already in .gitignore... "
	@for pattern in `cat .gitignore`; do find . -name "$$pattern" -delete; done
	@echo "OK!"

deploy-documentation: documentation
	@printf 'Deploying documentation ...'
	@echo "DONE!"

deploy: deploy-documentation

release: clean doctest deploy-documentation publish
	@printf "Exporting to $(filename)... "
	@tar czf $(filename) filetype setup.py README.md LICENSE
	@echo "DONE!"

lint:
	@flake8 .

publish:
	@python setup.py sdist register upload