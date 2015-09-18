#
# Copyright 2015 Yufei Li, Docloud Project
#

help:
	@echo "demo 临时命令，重新安装Docloud客户端"

demo:
	@pip uninstall docloud -y
	@pip install .

test:
	py.test -s -v tests/
