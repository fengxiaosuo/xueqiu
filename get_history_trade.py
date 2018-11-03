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
debug = 0
for line in stock_symbol_list_file:
	i=i+1
	if debug == 1 and i>3:
		break
	sympol = line.strip("\n")
	print sympol

	history_trade_file_name = "history_trade/"+sympol+".csv"
	history_trade_file = open(history_trade_file_name, "w+")	
	
	url = "http://quotes.money.163.com/service/chddata.html?code=1"+sympol+"&start=19910102&end=20171117&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
	if debug:
		print url
	
	html = get_html(url)

	if html == "":
		print "ERR: html get "+sympol+" failed!"
		continue
	else:	
		history_trade_file.write(html)

	history_trade_file.close()
	
stock_symbol_list_file.close()

print "INF: end of function"
