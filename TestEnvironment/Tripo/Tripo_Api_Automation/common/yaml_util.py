# -*- coding: UTF-8 -*-

import os

import yaml


def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml", encoding="utf-8", mode="r") as f:
        value=yaml.safe_load(f)
        return value[key]

def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8", mode="a+") as f:
        value=yaml.dump(data, stream=f, allow_unicode=True)

def clear_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()

#safe_load 有问题，一般是对应的yaml的内容格式有问题
def read_testcase(path):
    with open(os.getcwd() + "/"+path, encoding="utf-8", mode="r") as f:
        value = yaml.safe_load(f)
        return value
