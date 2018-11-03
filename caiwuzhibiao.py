#!/usr/bin/python
#coding=utf-8

import sys
import pycurl
import re
import StringIO
import urllib
import random

# get html from url
def get_html(url):
	b=StringIO.StringIO() 
	c=pycurl.Curl() 
	c.setopt(pycurl.URL, url) 
	c.setopt(pycurl.HTTPHEADER, ["Accept:"]) 
	c.setopt(pycurl.WRITEFUNCTION, b.write) 
	c.setopt(pycurl.FOLLOWLOCATION, 1) 
	c.setopt(pycurl.MAXREDIRS, 5) #指定HTTP重定向的最大数
	c.perform() 

	# check if we are OK
	if(c.getinfo(c.HTTP_CODE) == 200):
		html = b.getvalue()
	else:
		print "ERR: get_html failed. http code:" + str(c.getinfo(c.HTTP_CODE))
		html = ""
	b.close()
	c.close()
	return html

def get_list(html, patt=""):
	# define a re
	#<a href="/ershoufang/xicheng/"  title="北京西城在售二手房 ">西城</a>
	reg=r'<a href="/ershoufang/(.*?)/"  title="北京.{2,10}在售二手房 ">.{2,10}</a>'

	# find patt from html into list
	patt = re.compile(reg)
	list = re.findall(patt,html)

	'''
	print "INF: below are all members in list\n"
	for member in list:
		print "  "+member
		pass
	print "INF: end of list\n"
	'''
	
	return list

def search_patt(html, re):
	pass
###########################################################################
#
# main function start here
#
###########################################################################

# 准备工作
sympol = "000002"
stock_symbol_list_file = open("all_stocks2.csv","r")

i = 0
debug = 1
for line in stock_symbol_list_file:
	i=i+1
	if debug == 1 and i>3:
		break
	sympol = line.strip("\n")
	print sympol

	file0 = open("wangyi/"+sympol+"_lsjysj.csv", "w+")
	file1 = open("wangyi/"+sympol+"_zycwzb.csv", "w+")
	file2 = open("wangyi/"+sympol+"_cwbbzy.csv", "w+")
	file3 = open("wangyi/"+sympol+"_zcfzb.csv", "w+")
	file4 = open("wangyi/"+sympol+"_lrb.csv", "w+")
	file5 = open("wangyi/"+sympol+"_xjllb.csv", "w+")
	#历史交易数据
	url0 = "http://quotes.money.163.com/service/chddata.html?code=1"+sympol+"&start=19910102&end=20171117&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
	#主要财务指标
	url1 = "http://quotes.money.163.com/service/zycwzb_"+sympol+".html?type=report"
	#财务报表摘要
	url2 = "http://quotes.money.163.com/service/cwbbzy_"+sympol+".html"
	#资产负债表
	url3 = "http://quotes.money.163.com/service/zcfzb_"+sympol+".html"
	#利润表
	url4 = "http://quotes.money.163.com/service/lrb_"+sympol+".html"
	#现金流量表
	url5 = "http://quotes.money.163.com/service/xjllb_"+sympol+".html"
	if debug:
		print url0
		print url1
		print url2
		print url3
		print url4
		print url5
	
	html = get_html(url0)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
	else:	
		file0.write(html)
	
	html = get_html(url1)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
	else:	
		file1.write(html)
	
	html = get_html(url2)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
	else:	
		file2.write(html)
	
	html = get_html(url3)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
	else:	
		file3.write(html)
	
	html = get_html(url4)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
	else:	
		file4.write(html)
	
	html = get_html(url5)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
	else:	
		file5.write(html)
		
	file0.close()
	file1.close()
	file2.close()
	file3.close()
	file4.close()
	file5.close()
	
stock_symbol_list_file.close()

print "INF: end of function"
