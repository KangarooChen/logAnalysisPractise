#!/usr/bin/env python
# -*- coding: utf-8 -*-

'data capture module'

_author_ = 'kangaroo'

import re
import ex3
import os
import codecs

def get_log(logpath=''):

	month = '0'
	date  = '0'
	logtime  = '0'
	devtype  = '0'
	logtype  = '0'
	process  = '0'
	data  = '0'

	if not logpath:
		logpath = raw_input('Absolute path of logfile is needed:') #输入源日志文件的绝对路径
	analyfilename = os.path.splitext(os.path.split(logpath)[1])[0]+'_analysis'+os.path.splitext(os.path.split(logpath)[1])[1] #根据源文件名生成目标文件名
	analyfilepath = os.path.join(os.path.split(logpath)[0],analyfilename) #目标文件路径
	analyfile = codecs.open(analyfilepath,'w','utf-8')
	regular = r'(\w{3})\s+(\d{1,2})\s+(\d{2}\:\d{2}\:\d{2})\s+(\w*)\s+(\w*\.\w*)\s+(\w*\[\d*\])\:\s+(.*)' #匹配日志格式的正则表达式，7个分组
	re_itemize = re.compile(regular) #正则表达式预编译
	regular_808=r'client808\[\d*\]' #client808日志匹配规则
	re_808=re.compile(regular_808) #正则表达式预编译
	regular_data=r'.*(7[e|E].*7[e|E])'
	re_data=re.compile(regular_data)
	with open(logpath,'r') as log:
		n=1
		while n:
			line = log.readline()
			if line == '':
				break
			elif re_itemize.match(line):
				month = re_itemize.match(line).group(1)
				date  = re_itemize.match(line).group(2)
				logtime  = re_itemize.match(line).group(3)
				devtype  = re_itemize.match(line).group(4)
				logtype  = re_itemize.match(line).group(5)
				process  = re_itemize.match(line).group(6)
				data  = re_itemize.match(line).group(7)
			# print 'month:',month,'date:',date,'logtime:',logtime,'devtype:',devtype,'logtype:',logtype,'process:',process,'data:',data
			if re_808.match(process):
				if re_data.match(data):
					# print re_data.match(data).group(1)
					# print '=='*25
					prodata = re_data.match(data).group(1).replace(' ','').upper()
					prodata = prodata.replace('7D02','7E') #字符转义
					prodata = prodata.replace('7D01','7D') #字符转义
					ex3.protocal_analysis(prodata,month,date,logtime,analyfile)
		analyfile.close()

if __name__ == '__main__':
	get_log()