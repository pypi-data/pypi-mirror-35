#!/usr/bin/env python3
import json
import os
import codecs 
import numpy as np
import traceback
import pdb
import sys
sys.path.append("../")
import gensim
from gensimplus.source.gensim_plus_config import FLAGS
from gensimplus.source.model_save_load_helper import ModelSaveLoadHelper
from gensim.models import LsiModel
from gensim.models import LdaModel
from gensim.models import TfidfModel
import jieba
import jieba.posseg
import re
import numpy as np
import pdb
CURPATH = os.path.dirname(os.path.realpath(__file__))
import codecs

global global_cnt
global_cnt = 0
xiaoqu_names = []
with codecs.open(os.path.join(CURPATH,"../../data/gyxq2.txt"), "r",'GBK') as f:
    lines = f.readlines()
    xiaoqu_names = [re.sub("[\n\r]","",line) for line in lines]

left_txt = []

words2d = [
    ["富强","民主","文明","和谐","民主","文明","和谐"],
    ["自由","平等","公正","法治","法治"],
    ["爱国","敬业","明礼","诚信","敬业"]
]

words2d_eval = [
    ["富强","民主","文明"],
    ["自由","平等","公正"],
    ["爱国","敬业","敬业","敬业","发现"]
]

words = ["富强民主文明和谐", "自由平等公正法治", "爱国敬业明礼诚信"]

class RegHelper(object):
    def __init__(self):
        pass
        """
        lst = ['省','市','区','社区','居委会','自然村组','街路巷','门牌号', '建筑物名称','组团名称','楼层','栋号','楼栋名称','单元','楼层','户号']
        """
        print("\n> 实例化一个新的 TfidfHelper")
        self.reg_pools = []
        self.reg_pools_part_2 = []
        self.reg_pools.append([self.reg_gene(["省","县","镇(?!市)","[街道路巷]","号"]),'省','区','镇','街路巷','门牌号'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[街道路巷]","号","单元","号"]),'省','市','区','街路巷','门牌号','单元号','户号'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[街道路巷]","宿舍"]),'省','市','区','街路巷','组团名称'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[街道路巷]","号","栋","单元","号"]),'省','市','区','街路巷','门牌号','栋号','单元号','户号'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[乡镇]","村","组","号"]),'省','市','区','社区','村居委会','自然村组','号'])
        self.reg_pools.append([self.reg_gene(["省","县","镇(?!市)","市","村","组"]),'省','区','社区','村居委会','自然村组'])
        self.reg_pools.append([self.reg_gene(["省","市","办事处","村","组"]),'省','市','社区','村居委会','自然村组'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[街道路巷]","号","栋","单元","号"]),'省','市','区','街路巷名','门牌号','栋号','单元号','户号'])
        self.reg_pools.append([self.reg_gene(["省","县","乡","村","组"]),'省','县','社区','村居委会','自然村组'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[街道路巷]","号","栋","单元","号"]),'省','市','区','街路巷名','门牌号','[幢栋]','单元号','户号'])
        self.reg_pools.append([self.reg_gene(["省","市","(?<!小)区","[街道路巷]","号","栋","单元","号"]),'省','市','区','街路巷名','门牌号','[幢栋]','单元号','户号'])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号']),"省","市","区","街路巷名","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[乡镇](?!市)','村(?!民)','组','号']),"省","市","区","社区","村","组","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号','附\d+号']),"省","市","区","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','门牌号','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","门牌号","栋","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","栋","单元","楼层","户号"])
        #self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号','[\u4e00-\u9fa5]{1,3}','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","门牌号","栋","单元号","楼层","户号"])
        #贵州省贵阳市小河区黔江路18号黔江名典1栋4单元2楼2号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[乡镇]','村(?!民)','组']),"省","市","区","社区","村居委会","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[乡镇]','村(?!民)','组','号','附\d+号']),"省","市","区","社区","村居委会","自然村组","门牌号","户号"])
        #贵州省贵阳市花溪区久安乡吴山村白岩小寨组77号附3号
        self.reg_pools.append([self.reg_gene(['省','市','[乡镇]','村(?!民)','组']),"省","区","社区","村居委会","自然村组"])
        #贵州省清镇市站街镇鸡场堡村一组
        self.reg_pools.append([self.reg_gene(['省','市','[乡镇]','村(?!民)','组']),"省","区","社区","村居委会","自然村组"])
        #贵州省贵阳市云岩区白云大道192号广信四季家园25栋2单元2层1号
        self.reg_pools.append([self.reg_gene(['省','县','镇(?!)市','[街道路巷]','号','[幢栋]','单元','号']),"省","县","镇","街路巷名","门牌号","栋号","单元号","户号"])
        #贵州省修文县龙场镇民主路173号二栋二单元3号
        self.reg_pools.append([self.reg_gene(['省','市','镇','村(?!民)','组']),"省","区","社区","村居委会","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号','单元','楼',"号"]),"省","市","区","巷","号","单元号","楼层","户号"])
        #贵州省贵阳市云岩区浣沙巷18号1单元9楼附1号
        #贵州省清镇市站街镇中寨村一组
        #贵州省清镇市站街镇中寨村一组
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','大厦','[幢栋]',"号"]),"省","市","区","街路巷名","门牌号","建筑物名称","栋号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','办事处','村(?!民)','组','[街路巷]','号','附\d号']),"省","市","区","街路巷名","门牌号","建筑物名称","栋号","户号"])
        #贵州省贵阳市南明区遵义路64号智亿大厦2栋1202号
        #贵州省贵阳市花溪区清溪办事处花溪村五组清华路50号1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','办事处','村(?!民)','组','[街路巷]','号','附\d号']),"省","市","区",'社区',"村居委会","自然村组","街路巷名","门牌号","户号"])
        #贵州省贵阳市南明区遵义路64号智亿大厦2栋1202号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号','单元','楼','号']),"省","市","区","街路巷名","号","建筑物名称","栋号","户号"])
        #贵州省贵阳市云岩区浣沙巷18号1单元9楼附1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号','单元','楼','号']),"省","市","区","街路巷名","号","单元号","楼层","户号"])
        #贵州省贵阳市云岩区浣沙巷18号1单元9楼附1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','办事处','村(?!民)','组','路','号','附\d号']),"省","市","区","办事处","村","组","街路巷名","门牌号","户号"])
        #贵州省贵阳市花溪区清溪办事处花溪村五组清华路50号附1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','附\d号','楼']),"省","市","区","街路巷名","门牌号","户号","楼层"])
        #贵州省贵阳市乌当区富康路8号附61号5楼
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','[幢栋]','楼','号']),"省","市","区","街路巷名","门牌号","栋号","楼层","户号"])
        #贵州省贵阳市乌当区新创路12号5栋5楼1号
        self.reg_pools.append([self.reg_gene(['省','市','公司','生活区','[幢栋]','单元','楼','号']),"省","市","社区","居委会","栋号","单元号","楼层","户号"])
        #贵州省清镇市电建二公司二生活区17栋2单元2楼2号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','[幢栋]','单元','楼','号']),"省","市","社区","居委会","栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','[幢栋]','单元','附\d号']),"省","市","区","街路巷名","栋号","单元号","户号"])
        #贵州省贵阳市南明区五湖巷14栋1单元附1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','公司','分厂','[幢栋]','单元','附\d号']),"省","市","区","社区","居委会","栋号","单元号","户号"])
        #贵州省贵阳市花溪区贵州险峰实业总公司花溪分厂21栋2单元附4号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','段','号','[幢栋]','单元','附\d号']),"省","市","区","街路巷名","门牌号","栋号","单元号","户号"])
        #贵州省贵阳市南明区花溪大道北段242号9栋1单元附12号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','村(?!民)','[幢栋]','单元','附\d号']),"省","市","区","村居委会","栋","单元号","户号"])
        #贵州省贵阳市南明区贵棉村4栋1单元附77号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','[幢栋]','附\d号']),"省","市","区","街路巷名","门牌号","栋","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','[幢栋]','号']),"省","市","区","街路巷名","门牌号","栋","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','村(?!民)','[幢栋]','单元','号']),"省","市","区","村居委会","栋号","单元号","户号"])

        #贵州省贵阳市云岩区白云大道203号47栋16号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','办事处','村(?!民)','组','号']),"省","市","区","社区","村居委会","自然村组","户号"])
        #贵州省贵阳市花溪区溪北办事处竹林村五组6号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','镇(?!)市','区','[幢栋]','号']),"省","市","区","镇","社区","栋号","户号"])
        #贵州省贵阳市观山湖区金华镇敖凡冲煤矿四区9栋1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','花园','\d栋','单元','号']),"省","市","区","建筑物名称","栋号","单元号","户号"])
        #贵州省贵阳市观山湖区碧海花园碧海乾图9-2栋2单元1003号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','镇(?!)市','村(?!民)','组']),"省","市","区","镇","村居委会","自然村组"])
        #贵州省贵阳市花溪区石板镇合朋村大寨组2
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','镇(?!)市','村(?!民)','组','\d']),"省","市","区","镇","村居委会","自然村组",'户号'])
        #贵州省贵阳市花溪区石板镇合朋村大寨组2
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','镇(?!)市','村(?!民)','寨','号','附\d号']),"省","市","区","镇","村居委会","自然村组",'门牌号','户号'])
        #贵州省贵阳市花溪区青岩镇二关村刘家寨3号附1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','段','号','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","门牌号","栋",'单元号','楼','号'])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','段','号','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","门牌号","栋",'单元号','楼','号'])
        #贵州省贵阳市乌当区新添大道北段201号P栋2单元1楼1号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','苑','[幢栋]','单元','号']),"省","市","区","建筑物名","栋号",'单元号','户号'])
        #贵州省贵阳市观山湖区景怡西苑A7栋14单元401号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','村(?!民)','组']),"省","市","区","村","组"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','路','号','苑','[幢栋]','单元','号']),"省","市","区","路","号","建筑物名称","栋号","单元号","户号"])
        #贵州省贵阳市南明区观水路55号3栋2单元2503号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','路','号','[幢栋]','单元','号']),"省","市","区","路","号","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','厂','[幢栋]','单元','号']),"省","市","区","社区","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','小区','[幢栋]','单元','附\d+号']),"省","市","区","建筑物名称","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','路','号','单元','号']),"省","市","区","街路巷名","门牌号","单元号","户号"])
        #贵州省贵阳市白云区同心路24号五单元702号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','路','寨','[幢栋]','单元','附\d+号']),"省","市","区","街路巷名","建筑物名称","栋号","单元号","户号"])
        #贵州省贵阳市云岩区贵工路上寨8栋3单元附2号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','镇(?!)市','村(?!民)','[场寨组]','号']),"省","市","区","镇","村居委会","自然村组","户号"])
        #贵州省贵阳市花溪区青岩镇达夯村鼠场52号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','坡','号']),"省","市","区","街路巷名","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','小区','[幢栋]','单元','附\d号']),"省","市","区","建筑物名称","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','小区','[幢栋]','单元','号']),"省","市","区","建筑物名称","栋号","单元号","户号"])
        #贵州省贵阳市南明区黑坡18号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街道路巷]','号','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","门牌号",\
                "栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','办事处','村','队']),"省","市","区","社区","村居委会","自然村组",\
                "栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','[幢栋]','单元','[楼层]','号']),"省","市","区","街路巷名","门牌号","栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','路','号','[幢栋]','单元','楼','附\d号']),"省","市","区","街路巷名","门牌号","栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','路','号','[幢栋]','单元','楼','号']),"省","市","区","街路巷名","门牌号","栋号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','[幢栋]','单元','号']),"省","市","区","街路巷名","门牌号","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','号','号']),"省","市","区","街路巷名","门牌号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','[楼层]','号']),"省","市","区","街路巷名","门牌号","楼号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道坡]','号','单元','号']),"省","市","区","街路巷名","门牌号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道坡段]','号','[幢栋]','单元','号']),"省","市","区","街路巷名","门牌号","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道坡段]','号','[幢栋]','单元','号']),"省","市","区","街路巷名","门牌号","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','冲','号','单元','号']),"省","市","区","街路巷名","门牌号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','段','号','号']),"省","市","区","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','办事处','村','号','号']),"省","市","区","街路巷名","村居委会","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','段','号','单元','号']),"省","市","区","街路巷名","门牌号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','乡','委会','组','号','号']),"省","市","区","社区","村居委会","自然村组","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','乡','委会','组','号','号']),"省","市","区","社区","村居委会","自然村组","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','乡','委会','组','号','号']),"省","市","区","社区","村居委会","自然村组","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','巷','号','号']),"省","市","区","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','[街路巷道]','房','[幢栋]','单元','楼']),"省","区","村居委会","街路巷名","门牌号","建筑物名称","栋号","单元号","楼层"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','村']),"省","市","区","村居委会"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','组']),"省","市","区","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','村','组']),"省","区","社区","村居委会","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','[街路巷道]','号','号']),"省","市","区","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','公司','楼','[幢栋]','单元','号']),"省","市","社区","建筑物名称","栋号","单元号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','路','号']),"省","市","街路巷名","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','县','路','号']),"省","市","街路巷名","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','宿舍','号']),"省","市","村居委会","建筑物名称","户号"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','路','号','[幢栋]','号']),"省","市","村居委会","街路巷名","门牌号","栋号","户号"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','路','社区','号']),"省","市","村居委会","街路巷名","社区","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','路','号','号']),"省","市","村居委会","街路巷名","社区","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','县','[乡镇]','[街路巷道]','号','号']),"省","区","社区","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','县','[乡镇]','[街道巷路]','宿舍']),"省","区","社区","街路巷名","建筑物名称"])
        self.reg_pools.append([self.reg_gene(['省','市','路','号','号']),"省","市","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','花园','[楼栋]','单元','[楼层]','[号室]']),"省","市","建筑物名称","楼号","单元号","楼层","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','村','号']),"省","市","区","自然村组","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','[街道路巷]','号']),"省","市","街道路巷","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','县','[街道路巷]','号']),"省","区","街道路巷","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','[乡镇]','[街道路巷]','号']),"省","社区","街道路巷","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','河沟','[幢栋]','号']),"省","市","区","社区","栋号","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','河沟','[幢栋]','[楼层]','号']),"省","市","区","社区","栋号",'楼层',"门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','厂','[幢栋]',"单元",'[楼层]','号']),"省","市","区","社区","栋号","单元号",'楼层',"门牌号"])
        #贵州省贵阳市花溪区贵阳矿灯厂21栋1单元3楼5号
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','村','号','号']),"省","市","区","自然村组","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','市','路','号','号']),"省","市","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','路','号','号']),"省","区","社区","街路巷名","门牌号","户号"])
        self.reg_pools.append([self.reg_gene(['省','县','乡','村','组']),"省","区","社区","村居委会","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','委会']),"省","区","社区","村居委会"])
        self.reg_pools.append([self.reg_gene(['省','县','镇','村','沟']),"省","区","社区","村居委会","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','市','(?<!小)区','村','号']),"省","市","区","村居委会","门牌号"])
        self.reg_pools.append([self.reg_gene(['省','市','公司.+?楼','[栋幢]','号']),"省","市","建筑物名称","栋号","门牌号"])
        #self.reg_pools.append([self.reg_gene(['省','县','镇','村','[\u4e00-\u9fa5]{1,7}']),"省","区","社区","村居委会","自然村组"])
        self.reg_pools.append([self.reg_gene(['省','市','栋','单元','楼']),"省","市","栋号","单元号","楼层"])
        self.reg_pools.append([self.reg_gene(['省','市','路']),"省","市","路"])
        #self.reg_pools.append([self.reg_gene(['省','市','区','路','[\u4e00-\u9fa5]{1,7}']),"省","市","街路巷名","建筑物名称"])
        self.reg_pools.append([self.reg_gene(['省','市','区','社区服务中心','居委会','[街路巷道]','号','栋','号']),"省","市","区","社区","村居委会","街路巷名","门牌号","栋号","户号"])
        self.reg_pools.append([self.reg_gene(['市','区','服务中心','(?:委会|委会服务中心)','[街路巷道段]','号','栋','\d+']),"市","区","社区","村居委会","街路巷名","门牌号","栋号","户号"])
        #pattern = re.compile(r'(.*?省)(.*?市)?(.*?(?<!小)区)?(.*?(?:乡|镇|办事处|社区服务中心))?'r'(.*?村)?(.*?[路巷街])?(?:(?<=[路巷街])(\d+号)?)?(附?[\da-zA-Z]+(?:栋|幢|号楼))')
        #self.reg_pools_part_2.append([pattern,"省","市","区","社区","村居委会","街路巷名","门牌号","栋号"])
        #pattern = re.compile(r'^(.{2,4}省)?(.{2,5}市)?(.+?(?:(?<!小)区|县))?(.+?(?:乡|镇(?!委会)|办事处|社区服务中心|服务中心|路社区服务中心))?(.+?(?:村|坡|委会))?(.+?(?:路|巷|街|道|(?<=[东南西北中])段))?(.+?组)?(.+?号(?!楼))?(.+?号楼)?(.+?[幢栋])?(.+?(?:车辆厂|工厂|公司))?(.+?单元)?(.+?层)?([附]{0,1}.+?[号室]{0,1})?$')
        #pattern = re.compile(r'^(.{2,4}省)?(.{2,5}市)?(.+?(?:(?<!小)区|县))?(.+?(?:乡|镇(?!委会)|办事处|社区服务中心))?(.+?(?:村委会服务中心|村委会|村|村委员会|居委会))?(?:.+?村)?(.+?[段街路巷道])?(.+?组(?!团))?((?:散居)?\d+号(?!楼)(?:附\d+号)?)?([\u4e00-\u9fa5]{0,9})(\d+(?:组团|区|期))?(\d+号楼)?([\da-zA-Z]+?[幢栋])?(.+?(?:车辆厂|工厂|公司))?([\d一-十]+?单元)?(\d+[楼层])?(附?\d+[号室]?|散居\d+|\d+)?$')
        pattern = re.compile(r'^(.{2,4}省)?(.{2,5}市)?(.+?(?:(?<!小)区|县))?(.+?(?:乡|镇(?!委会)|办事处|社区服务中心))?(.+?(?:村委会服务中心|村委会|村|村委员会|居委会))?(?:.+?村)?(.+?[段街路巷道])?(.+?组(?!团))?((?:散居)?\d+号(?!楼)(?:附\d+号)?)?([\u4e00-\u9fa5]{0,9}(?=[\d一-十a-zA-Z]{2,}))?(\d+(?:组团|区|期))?(\d+号楼)?([\da-zA-Z]+?[幢栋])?([\d一-十]+?单元)?(\d+[楼层])?(附?\d+[号室]?|散居\d+|\d+)?$')
        self.reg_pools_part_2.append([pattern,"省","市","区","社区","村居委会","街路巷名","自然村组","门牌号","小区名称","组团名称","楼号","栋号","单元号","层","户号"])
        CURPATH = os.path.dirname(os.path.realpath(__file__))
        fl = os.path.join(CURPATH,"reg_rule_from_doc_3.txt")
        self.create_reg_from_doc(fl)

        #贵州省清镇市地勘天虹花园2栋3单元2层1号

        """
        city=市------地级市、直辖市
        county=区（市、县）------------区、县、地级市下的县级市；

        贵阳市清镇市         贵阳市=市       清镇市=区（市、县）；
        province=省
        city=市
        county=区（市、县）
        community=社区（乡、镇）
        committee=居（村）委员会
        village=自然村组
        street=街路巷
        doornum=门牌号
        groupname=组团名称
        buildname=建筑物名称
        lno=楼号
        dno=栋号
        unit=单元
        floor=楼层
        room=户室
        """

        #self.reg_pools = sorted(self.reg_pools,reverse=False)
        #pdb.set_trace()

    def create_reg_from_doc(self,docpath):
        f = codecs.open(docpath,"r","utf-8")
        lines = f.readlines()
        for line in lines:
                line = re.sub("[\n\r ]","",line)
                parts = line.split("aaa")
                if not len(parts) == 2:
                    continue
                p0 = parts[0].split(",")
                p1 = parts[1].split(",")
                #print(parts)
                #pdb.set_trace()
                if not len(p0) == len(p1):
                    continue
                p1.insert(0,self.reg_gene(p0))
                #pdb.set_trace()
                self.reg_pools.append(p1)
        f.close()

    def reg_gene(self,txtLst):
        regexp = ""
        for i in txtLst:
            if i in ['散居','[幢栋]','单元','楼','号','号','附\d号','附\d+号','栋']:
                regexp+="([附付\d甲乙丙丁一二三四五六七八九十a-zA-Z-]{1,7}%s)"%i
            elif i in [r'\d',r'\d+',r'(?:\d|号)']:
                regexp+="(\d+%s)"%i
            elif i in ['镇','村','组']:
                regexp+="(.{1,4}%s(?!居委会))"%i
            elif i in ['路','道','巷','街','[街道路巷段]','[街路巷道]','[街道路巷]','[街路巷道段]']:
                regexp+="([^村]{1,4}%s(?!(?:服务中心|社区服务中心|商业步行街)))"%i
            elif i in ['市','省','县','乡','镇']:
                regexp+="(.{1,7}%s)"%i
            elif i in ['委会']:
                regexp+="(.{1,7}(?:委会|委会服务中心))"
            elif i in ['区']:
                regexp+="(.{1,7}(?:(?<!i[小社])区(?!服务中心)))"
            else: 
                regexp+="(.{1,7}%s)"%i
        #print(regexp)
        return "^"+regexp+"$"

    def reg_factory(self,intxt):
        kw = "省市区路号社区栋乡镇县幢单元楼层号室乡村组寨坡"
        outtxt = re.sub("[^%s]"%kw,"",intxt)
        return outtxt

    def address_formula(self,txt):
        global global_cnt
        maxlen = 0
        base = {}
        base_exp = ""
        for exp in self.reg_pools:
            resJson = {}
            res = re.findall(exp[0],txt)
            if len(res)>0:
                for k,v in zip(exp[1:],res[0]):
                    resJson[k] = v
                if len(resJson)>0:
                    #print(txt,"\n",global_cnt,"\n",resJson,"\n",exp[0])
                    #pdb.set_trace()
                    if len(resJson) > maxlen:
                        maxlen = len(resJson)
                        base = resJson
                        base_exp = exp[0]
        if base == {}:
            resJson2 = {}
            res = list(re.findall(self.reg_pools_part_2[0][0],txt))
            if len(res)>0:
                res = res[0]
            #pdb.set_trace()
            if len(res) < 3:
                global_cnt+=1
            else:
                for m,n in zip(res,self.reg_pools_part_2[0][1:]):
                    resJson2[n] = m 
                base = resJson2
            with open("./fail_address.txt","a+") as f:
                f.write(txt)
                f.write("\n")
                f.write(str(base))
                f.write("\n")
                f.write(str(base_exp))
                f.write("\n")
        outbase = self.double_check(base)
        with open("./succ_address.txt","a+") as f:
            pass
            f.write(txt)
            f.write("\n")
            f.write(str(outbase))
            f.write("\n")
            f.write(str(base_exp))
            f.write("\n")
            f.write("=======")
            f.write("\n")
        #pdb.set_trace()
        print(txt,"\n",global_cnt,"\n",outbase)
        return outbase 

    def double_check(self,inbase):
        base = inbase.copy()
        #print(base)
        kws = ['组团名称','建筑物名称','小区名','省','市','区','社区','村居委会','自然村组','栋号','楼层','户号','单元号','楼号','门牌号','街路巷名']
        mapkv = {}
        mapkv['[街路巷道段]'] = "街路巷名"
        mapkv['街路巷'] = "街路巷名"
        mapkv['服务中心'] = "社区"
        mapkv['委会'] = "村居委会"
        mapkv['街路巷道'] = "街路巷名"
        mapkv['街道路巷'] = "街路巷名"
        mapkv['建筑物'] = "建筑物名称"
        mapkv['建筑物名'] = "建筑物名称"
        mapkv['巷'] = "街路巷名"
        mapkv['道'] = "街路巷名"
        mapkv['街区'] = "街路巷名"
        mapkv['路'] = "街路巷名"
        mapkv['段'] = "街路巷名"
        mapkv['号'] = "门牌号"
        mapkv['乡'] = "社区"
        mapkv['镇'] = "社区"
        mapkv['村'] = "村居委会"
        mapkv['组'] = "自然村组"
        mapkv['县'] = "区"
        mapkv['栋'] = "栋号"
        mapkv['幢'] = "栋号"
        mapkv['层'] = "楼层"
        mapkv['楼'] = "楼层"
        mapkv['单元'] = "单元号"
        mapkv['室'] = "户号"
        mapkv['社'] = "村居委会"
        mapkv['公司'] = "小区名"
        mapkv['组(?!团)'] = "自然村组"
        mapkv['社区服务中心'] = "社区"
        mapkv['[街路巷爱道]'] = "街路巷名"
        mapkvLst = [str(k) for k in mapkv]
        #pdb.set_trace()
        for k in inbase:
            #k = re.sub("[^\u4e00-\u9fa5]","",k)
            v = ""
            if k in mapkvLst:
                v = mapkv[k]
                #print(k,v)
                base[v] = base[k]
                base.pop(k)
            else:
                v = k
            if not v in kws:
                print(mapkvLst,v)
                #pdb.set_trace()
            else:
                pass
            if v == "市":
                if base[v] in ["贵阳","贵阳市","六盘水","六盘水市","遵义市","遵义","安顺","安顺市","铜仁","铜仁市","毕节市","毕节"]:
                    pass
                else:
                    base['区'] = base[v]
                    #print("\n===\n",base[v],v)
                    base.pop(v)
                    #print(base)
                    #pdb.set_trace()
            if v in base and '小区' in base[v]:
                #print(v)
                if v == "小区名":
                    pass
                else:
                    base["小区名"] = base[v]
                    base.pop(v)

            if "街路巷名" in base:
                print(v, base['街路巷名'])

            """
            if v in base:
              if '社区服务中心' in base[v]:
                print(v, base[v])
                resLst = base[v].split("社区服务中心")
                if len(resLst) == 2 and resLst[1] == "":
                    if not v == "社区":
                        base.pop(v)
                        base["社区"] = base[v]
                elif len(resLst) == 2 and len(resLst[1])>0:
                    base["社区"] = "%s%s"%(resLst[0],"社区服务中心") 
                    if v == "社区":
                        print("alarm there r 2 社区")
                        base["街路巷名"] = "%s"%(resLst[1]) 
                    else:
                        base[v] = "%s"%(resLst[1]) 
                else:
                    pass

            if v in base and '居委会' in base[v]:
                print(v)
                resLst = base[v].split("居委会")
                if len(resLst) == 2 and resLst[1] == "":
                    if not v == "村居委会":
                        base["村居委会"] = base[v]
                        base.pop(v)
                elif len(resLst) == 2 and len(resLst[1])>0:
                    base["村居委会"] = "%s%s"%(resLst[0],"居委会") 
                    if v == "村居委会":
                        print("alarm there r 2 村居委会")
                        base["街路巷名"] = "%s"%(resLst[1]) 
                    else:
                        base[v] = "%s"%(resLst[1]) 
                else:
                    pass
            """
        outbase = base.copy()
        for k in base:
            if base[k] == "":
                outbase.pop(k)
        outbase = self.xiaoqu_check(outbase)
        print("doublecheck",outbase)
        return outbase

    def xiaoqu_check(self,outbase):
        tmp = outbase.copy()
        for item in outbase:
            for name in xiaoqu_names:
                if name in outbase[item]:
                    if "居委会" in outbase[item] or "中心" in outbase[item] or "办事处" in outbase[item]:
                        return tmp
                    tmp[item] = re.sub(name,"",outbase[item])
                    tmp["小区名"] = name
        return tmp

    def rules_cover_cnt(self,rule):
        cnt = 0
        with open("/home/distdev/iba/dmp/gongan/address_formula/data/address2.txt","r") as f:
            lines = f.readlines()
            np.random.shuffle(lines)
            for line in lines[:10000]:
                #pdb.set_trace()
                res=re.findall(rule[0],line)
                if len(res)>0:
                    cnt+=1
        #print(cnt, rule[0])

    def wr_lst(self,lst,filename):
        with open(filename,'a+') as f:
            for line in lst:
                f.write(line)
                f.write("\n")

    def chunked_sents(self):
        rt = []
        wr = []
        filename = "/home/distdev/iba/dmp/gongan/address_formula/address_formula.json"
        with open(filename,"r") as f:
            cont = f.read()
            kv = json.loads(cont)
            for k in kv:
                if len(wr)>10:
                    break
                #pdb.set_trace()
                sent = kv[k]['sent']
                reskv = self.address_formula(sent)
                for kk in kv[k]:
                    try:
                        reskv[kk]
                    except KeyError:
                        wr.append(sent)
                        break
                    if kk == "sent":
                        continue
                    elif kv[k][kk] == reskv[kk]:
                        pass
                    else:
                        wr.append(sent)
                        wr.append(kv[k][kk])
                        wr.append(reskv[kk])
                        wr.append("====")
                        break
                rt.append(sent)
                #pdb.set_trace()
        self.wr_lst(wr,"./wrong_result.txt")
        #self.wr_lst(rt,"./wrong_result.txt")
        print(len(rt),len(wr),100*len(wr)/len(rt))
        return wr,rt

    def eval_one(self,dctin):
            print(dctin['sent'])
            kv = {}
            kv = self.address_formula(dctin['sent'])
            kv['sent'] = dctin['sent']
            print("out",kv)
            for k in dctin:
                if k in kv:
                    if dctin[k] == kv[k]:
                        continue
                    else:
                        print(k,dctin[k],kv[k])
                        #pdb.set_trace()
                        self.wr_lst([str(kv)],"eval_score.txt")
                        self.wr_lst([kv['sent']],"fail_address.txt")
                        return False
            if len(kv) == 1:
                self.wr_lst([str(kv)],"eval_score.txt")
                self.wr_lst([kv['sent']],"fail_address.txt")
                return False
            #pdb.set_trace()
            return True 

    def eval_file(self):
            rcnt,wcnt = 0.0,0.0
            with open("../../data/address_formula.json","r") as f:
                cont = json.loads(f.read())
                klst = [k for k in cont]
                np.random.shuffle(klst)
                for k in klst:
                    item = cont[k]
                    if not "栋" in item['sent']:
                        #pdb.set_trace()
                        continue
                    print("input",item)
                    flag = self.eval_one(item)
                    if flag:
                        rcnt+=1.0
                    else:
                        wcnt+=1.0
                        self.wr_lst([str(item)],"eval_score.txt")
                        self.wr_lst(["==========="],"eval_score.txt")
                    if wcnt > 20:
                        break
                    print(wcnt,"is more than 20, when wcnt")
                    if wcnt %1 == 0:
                        print(rcnt, wcnt)
            acc = rcnt/(rcnt+wcnt+0.1)
            print(rcnt, wcnt, acc)

if __name__ == "__main__":
   txt = "贵州省贵阳市白云区安庆巷10号一单元7号"
   txt = "贵州省修文县扎佐镇中山南路38号"
   txt = "贵州省贵阳市白云区安庆巷10号二单元10号"
   txt = "贵州省贵阳市白云区粑粑坳"
   txt = "贵州省贵阳市白云区都拉乡都拉村中寨组25号附2号"

   #pdb.set_trace()
   f = ""
   if len(sys.argv)>1:
       mtd = sys.argv[1]
       act = sys.argv[2]
   regHelperInstance = RegHelper() 
   if act == "DEBUG":
      pdb.set_trace()
      f = codecs.open("./fail_address.txt","r","utf-8") 
      #f = codecs.open("/home/distdev/iba/dmp/gongan/address_formula/data/fail_address.txt","r","utf-8") 
      pdb.set_trace()
   elif act == "RUN":
      f = codecs.open("/home/distdev/iba/dmp/gongan/address_formula/data/addr_focus.txt","r","utf-8") 
   elif act == "CHUNK":
      res = regHelperInstance.chunked_sents()
      pdb.set_trace()
   elif act == "eval":
      pdb.set_trace()
      regHelperInstance.eval_file()
   #for rule in regHelperInstance.reg_pools:
   #    cnt = regHelperInstance.rules_cover_cnt(rule)

   #with codecs.open("/home/distdev/iba/dmp/gongan/address_formula/data/wrong_address.txt","r","utf-8") as f:
   lines = f.readlines()
   np.random.shuffle(lines)
   cntcnt = 0
   for line in lines[:3000]:
       #if not '塔' in line:
       #if not "栋" in line and not "居委会" in line and not '塔' in line:
       #    continue
       #rs = re.findall(".{2,3}省.{1,3}市.{2,3}区.{1,2}路\d+号",line)
       #if len(line)<25:
       #    continue
       rs = regHelperInstance.address_formula(line)
       cntcnt+=1
       if cntcnt%10000 == 0:
           print(cntcnt)
   f.close()
   with open("new_address.txt","a+") as f:
       for line in left_txt:
           pass
           f.write(line)
           f.write("\n")

   print(global_cnt)
   #pdb.set_trace()

