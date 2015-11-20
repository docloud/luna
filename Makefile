#
# Copyright 2015 Yufei Li, Luna Project
#

help:
	@echo "develop      Init project environment"
	@echo "document     Build Document file"
	@echo "test         Run test cases."
	@echo "cov          Run coverage statistic."

develop:
	pip install -e .

test:
	py.test -s -v tests/

coverage:
	py.test -s -v --cov=tests --cov-report=html

document:
	luna build document

publish-document:
	@ghp-import docs/_book -p -n -b gh-pages
