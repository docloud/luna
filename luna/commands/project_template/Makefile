#
# Copyright 2015 {{project}}
#

help:
	@echo "develop      Init project environment"
	@echo "document     Build Document file"
	@echo "test         Run test cases."

develop:
	@pip install -e .

test:
	py.test -s -v tests/

document:
	luna build document
