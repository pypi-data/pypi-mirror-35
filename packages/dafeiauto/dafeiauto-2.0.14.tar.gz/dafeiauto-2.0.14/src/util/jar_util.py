#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
from jpype import *
from src.util import get_root_path
import jpype, os.path

JVMPATH = jpype.getDefaultJVMPath()
ROOTPATH = get_root_path.get_root_path()


class Jar(object):
    @classmethod
    def get(cls, params):
        callback = {}
        jar_class = ""
        for i, j in params.items():
            name = os.path.join(ROOTPATH, "lib\\jar\\" + i + ".jar")
            jar_class += ";" + name
        jpype.startJVM(JVMPATH, "-ea", "-Djava.class.path=%s" % (jar_class))
        for i, j in params.items():
            callback[i] = jpype.JClass(j)()
        return callback

    @classmethod
    def close(cls):
        if isJVMStarted():
            jpype.shutdownJVM()
