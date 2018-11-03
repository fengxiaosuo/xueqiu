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

def get_stock_sympol_list(source_file, source_file2):	
	#1,平安银行,000001.XSHE
	#2605,川投能源,600674.XSHG
	reg=r'[0-9]*,.*?,([0-9]*).(XSHE|XSHG)'
	patt = re.compile(reg)
	
	list = []
	for line in source_file:
		print line
		result = re.search(patt,line)
		if result:
			print "result="+result.group(1)+result.group(2)
			if(result.group(2) == "XSHE"):
				#list.append("SZ"+result.group(1))
				#source_file2.write("SZ"+result.group(1)+"\n")
				list.append(result.group(1))
				source_file2.write(result.group(1)+"\n")
			elif(result.group(2) == "XSHG"):
				#list.append("SH"+result.group(1))
				#source_file2.write("SH"+result.group(1)+"\n")
				list.append(result.group(1))
				source_file2.write(result.group(1)+"\n")
	return list
	
###########################################################################
#
# main function start here
#
###########################################################################

# 准备工作
company_list = []
company_list_file = open("company_list.csv", "w+")
stock_symbol_list_file = open("all_stocks.csv","r")
stock_symbol_list_file2 = open("all_stocks2.csv","w+")

stock_symbol_list = get_stock_sympol_list(stock_symbol_list_file, stock_symbol_list_file2)

#https://xueqiu.com/S/SZ000002
#https://xueqiu.com/S/SH600979

company_list_file.close()
stock_symbol_list_file.close()
stock_symbol_list_file2.close()
print "INF: end of function"
