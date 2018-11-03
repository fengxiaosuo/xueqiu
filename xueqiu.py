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
company_list = []
company_list_file = open("company_list.csv", "w+")
stock_symbol_list_file = open("all_stocks2.csv","r")
#https://xueqiu.com/S/SZ000002
#https://xueqiu.com/S/SH600979

i = 0
for line in stock_symbol_list_file:
	i=i+1
	if i>3:
		break
	sympol = line.strip("\n")
	print sympol
	#url = "https://xueqiu.com/S/"+sympol+"/GSJJ"
	url = "https://xueqiu.com/"
	print url
	
	html = get_html(url)
	if html == "":
		print "ERR: html get "+sympol+" failed!"
		continue
	else:
		#"<strong class="stockName"> <a href="https://xueqiu.com/S/SZ000002" title="China Vanke CO.,LTD.">万科A(SZ:000002)</a></strong>"
		patt = re.compile(r'<strong class="stockName">.*?\((SH|SZ):(\d{6})\)</a></strong>')
		result = re.search(patt,html)
		if result:
			#csv_file.write(result.group(1)+",")
			print "INF: "+result.group(1)
		else:
			#csv_file.write(",,")
			print "ERR: no found"

			

company_list_file.close()
stock_symbol_list_file.close()

print "INF: end of function"
