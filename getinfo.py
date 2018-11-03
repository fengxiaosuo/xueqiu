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
csv_file = open("company_list.csv", "w+")
stock_symbol_list_file = open("all_stocks2.csv","r")

csv_file.write("公司名称,所属地域,涉及概念,主营业务,上市日期,每股净资产,每股收益,净利润,净利润增长率,营业收入,每股现金流,每股公积金,每股未分配利润,总股本,流通股\n")
i = 0
debug = 0
for line in stock_symbol_list_file:
	i=i+1
	if debug == 1 and i>3:
		break
	sympol = line.strip("\n")
	print sympol

	url = "http://stockpage.10jqka.com.cn/"+sympol+"/"
	print url
	
	html = get_html(url)

	if html == "":
		print "ERR: html get "+sympol+" failed!"
		continue
	else:
		patt = re.compile(r'<dt>公司名称：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
		
		patt = re.compile(r'<dt>所属地域：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"

		patt = re.compile(r'<dt>涉及概念：</dt>[\s\S]+?<dd title="(.*?)">.*?</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"

		patt = re.compile(r'<dt>主营业务：</dt>[\s\S]+?<dd>.*?</dd>[\s\S]+?<dd title="[\s\S]+?(.*?)">.*?</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"

		patt = re.compile(r'<dt>上市日期：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>每股净资产：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>每股收益：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>净利润：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>净利润增长率：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>营业收入：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>每股现金流：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>每股公积金：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>每股未分配利润：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>总股本：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
		patt = re.compile(r'<dt>流通股：</dt>[\s\S]+?<dd>(.*?)</dd>')
		result = re.search(patt,html)
		if result:
			csv_file.write(result.group(1)+",")
			if debug:
				print "INF: "+result.group(1)
		else:
			csv_file.write(",,")
			if debug:
				print "ERR: no found"
			
			
			
			
			
			
			
			
			
			
			
	csv_file.write("\n")
	print "\n"
	
csv_file.close()
stock_symbol_list_file.close()

print "INF: end of function"
