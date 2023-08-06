#!/usr/bin/env python3
import os
import codecs 
import numpy as np
import traceback
import pdb
import sys
import gensim_plus_config as conf
import nltk
from nltk import corpus

CURPATH = conf.CURPATH

class ChunkParser(object):

    def __init__(self):
        pass

    #def newRegexParser(self,sentence="贵阳省贵州市",grammer=r"^(.*?省)?(.*?市)?(.*?[区县])?.+?$"):
    def newRegexParser(self,sentence="abc",grammer=r"a"):
        cp = nltk.RegexpParser(grammer)
        result = cp.parse(sentence)
        print(result)
        pdb.set_tarce()

if __name__ == "__main__":
    pass
    cpInstance = ChunkParser()
    cpInstance.newRegexParser(sentence="abc",grammer=r"a")
    cmd = sys.argv[1]
    para = sys.argv[2]
    method_dict = {}
    method_dict['newRegexParser'] = cpInstance.newRegexParser
    if cmd == "-r":
        method_dict['newRegexParser'](*tuple(sys.argv[3:]))

