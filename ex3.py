#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a analysis module'

_author_ = 'kangaroo'

import re
import codecs
counter = 1

def protocal_analysis(prodata,month='Sep',date='30',logtime='23:59:59',analyfile=''):
	if analyfile == '':
		analyfile=codecs.open('f:\\test_analy.log','w','utf-8')
	mid = prodata[2:6] #消息ID
	if mid == '0200':
		mattr = int(prodata[6:10],16) #消息属性
		pnumb = prodata[10:22] #手机号码
		flowid = prodata[22:26] #消息流水号
		alarmsign = int(prodata[26:34],16) #报警标志
		status = int(prodata[34:42],16) #状态
		latitude = int(prodata[42:50],16) #纬度
		longtitude = int(prodata[50:58],16) #经度
		height = int(prodata[58:62],16) #高程
		speed = int(prodata[62:66],16) #速度
		orientation = int(prodata[66:70],16) #方向
		mtime = prodata[70:82] #消息时间
		global counter
		print counter
		analyfile.write(str(counter)+'\n')
		counter += 1
		analyfile.write(u'日志时间： %s/%s\t%s\n' %(month,date,logtime))
		# print u'消息ID： %s\n消息属性： %s\n手机号码： %s\n流水号： %s\n报警标志： %s\n状态： %s\n纬度： %s\n经度： %s\n高程： %s\n速度： %s\n方向： %s\n时间： %s\n'  % (mid,mattr,pnumb,flowid,alarmsign,status,latitude,longtitude,height,speed,orientation,mtime)
		# print len(bin(status)[2:])

		print u'消息ID： %s\n消息属性： %s'  % (mid,mattr)
		analyfile.write(u'消息ID： %s\n消息属性： %s\n' % (mid,prodata[6:10])) #输出文件显示十六进制数
		mattr_string = mattr_analysis(bin(mattr)[2:])
		analyfile.write(mattr_string)
		print u'手机号码： %s\t流水号： %s' %(pnumb,flowid)
		analyfile.write(u'手机号码： %s\t流水号： %s\n' %(pnumb,flowid))
		print u'报警标志： %s' % alarmsign
		analyfile.write(u'报警标志： %s\n' % prodata[26:34]) #输出文件显示十六进制数
		alarmsign_string = alarmsign_analysis(bin(alarmsign)[2:])
		print alarmsign_string
		if not alarmsign_string == '':
			analyfile.write(alarmsign_string)
		print u'状态： %s' % status
		analyfile.write(u'状态： %s\n' % prodata[34:42]) #输出文件显示十六进制数
		status_string = status_analysis(bin(status)[2:])
		analyfile.write(status_string)
		print u'纬度：%s\t经度：%s\t高程：%s\t速度：%s\t方向：%s\n时间：%s' % (latitude,longtitude,height,speed,orientation,mtime)
		analyfile.write(u'纬度：%s\t经度：%s\t高程：%s\t速度：%s\t方向：%s\n位置信息时间：%s\n' % (latitude,longtitude,height,speed,orientation,mtime))
		print '='*20
		analyfile.write(u'='*20+'\n')
		add_prodata = prodata[82:-4]
		add_string = addition_analysis(add_prodata)
		analyfile.write(add_string)


#报警信息解析函数
def alarmsign_analysis(alarmsign):
	n = len(alarmsign)
	s = ''
	context = {0:u'紧急报警', 1:u'超速报警', 2:u'疲劳驾驶', 3:u'危险预警', 4:u'GNSS模块发生故障', 5:u'GNSS天线未接或被剪断', 6:u'GNSS天线短路', 7:u'终端主电源欠压', 8:u'终端主电源掉电', 9:u'终端LCD或显示器故障', 10:u'TTS模块故障', 11:u'摄像头故障', 12:u'道路运输证卡模块故障', 13:u'超速预警', 14:u'疲劳驾驶预警', 15:u'保留', 16:u'保留', 17:u'保留', 18:u'当天累计驾驶超时', 19:u'超时停车', 20:u'进出区域', 21:u'进出路线', 22:u'路段行驶时间不足/过长', 23:u'路线偏离报警', 24:u'车辆', 25:u'车辆油量异常', 26:u'车辆被盗', 27:u'车辆非法点火', 28:u'车辆非法位移', 29:u'碰撞预警', 30:u'侧翻预警', 31:u'非法开门报警'}
	for m in range(n):
		if int(alarmsign[-1-m],2):
			print m,context[m]
			s = s + u'\t%s\t%s' %(m,context[m])
	if not s == '':
		return s+'\n'
	else:
		return s
	
#状态位解析函数
def status_analysis(status):
	n = len(status)
	s =u''
	context_0 = {0:u'ACC关', 1:u'未定位', 2:u'北纬', 3:u'东经', 4:u'运营状态', 5:u'经纬度未经保密插件加密', 6:u'保留', 7:u'保留', 10:u'车辆油路正常', 11:u'车辆电路正常', 12:u'车门解锁', 13:u'门1关', 14:u'门2关', 15:u'门3关', 16:u'门4关', 17:u'门5关', 18:u'未使用GPS卫星进行定位', 19:u'未使用北斗卫星进行定位', 20:u'未使用GLONASS卫星进行定位', 21:u'未使用Galileo卫星进行定位', 22:u'保留', 23:u'保留', 24:u'保留', 25:u'保留', 26:u'保留', 27:u'保留', 28:u'保留', 29:u'保留', 30:u'保留', 31:u'保留'}
	context_1 = {0:u'ACC开', 1:u'定位', 2:u'南纬', 3:u'西经', 4:u'停运状态', 5:u'经纬度已经保密插件加密', 6:u'保留', 7:u'保留', 10:u'车辆油路断开', 11:u'车辆电路断开', 12:u'车门加锁', 13:u'门1开（前门）', 14:u'门2开（中门）', 15:u'门3开（后门）', 16:u'门4开（驾驶席门）', 17:u'门5开（自定义）', 18:u'使用GPS卫星进行定位', 19:u'使用北斗卫星进行定位', 20:u'使用GLONASS卫星进行定位', 21:u'使用Galileo卫星进行定位', 22:u'保留', 23:u'保留', 24:u'保留', 25:u'保留', 26:u'保留', 27:u'保留', 28:u'保留', 29:u'保留', 30:u'保留', 31:u'保留'}
	context_89 ={'00':u'空车','01':u'半载','10':u'保留','11':u'满载'}
	for m in range(n):
		if m==8:
			print '8/9',context_89[status[-10:-8]]
			s = s + u'8/9\t%s' %context_89[status[-10:-8]]
		elif m==9:
			pass
		elif int(status[-1-m],2):
			print m,context_1[m]
			s = s + u'\t%s\t%s' %(m,context_1[m])
		else :
			print m,context_0[m]
			s = s + u'\t%s\t%s' %(m,context_0[m])
	# print '='*25
	return s+'\n'

#消息属性解析函数
def mattr_analysis(mattr):
	n = len(mattr)
	s =u''
	if n<16:						#补零
		for i in range(1,17-n):
			mattr = '0'+mattr
	msglen = int(mattr[-10:],2)
	print u'消息体长度：', msglen
	s =  s + u'\t消息体长度：%s ' %msglen
	# s='消息体长度：%s'  %msglen
	if int(mattr[-13:-10],2):
		print u'加密方式：RSA'
		s = s + u'\t加密方式：RSA'
	else:
		print  u'加密方式：不加密'
		s = s + u'\t加密方式：不加密'
	if int(mattr[-14:-13],2):
		print u'分包：是'
		s = s + u'\t分包：是'
	else:
		print u'分包：否'
		s = s + u'\t分包：否'
	# print '='*25
	return s+'\n'


#附加信息解析函数
def addition_analysis(add_prodata):
	add_len = len(add_prodata)
	s = u''
	j = 0
	while j<add_len:
		add_proid = add_prodata[j:j+2]
		print u'消息ID：',add_proid
		s = s + u'消息ID：%s\n' % add_proid
		add_prolen = int(add_prodata[j+2:j+4],16)
		print u'消息长度：',add_prolen
		s = s + u'消息长度：%s\n' % add_prolen
		add_procox = add_prodata[j+4:j+4+add_prolen*2]
		print u'消息内容：',add_procox
		s = s + u'消息内容：%s\n' % add_procox
		j = j+4+add_prolen*2
	print '=='*20
	s = s + u'=='*20+'\n'
	return s

if __name__ == '__main__':
	# protocal_analysis('7E02000066075533180001108100080000000C000301599F7A06CD2B9800B100000000151008120351E1040000000FE20400000000E604000000FEE70C000000040000000000000000010400000B4C02020000030200002504000000002A0200002B0401C201C2300105310109E004E4020000267E')
	protocal_analysis('7E02000084013800000002007700000000000C2001000000000000000000000000000015102814173101040000000003020000250402000000310100140400000005E1040000000FE20400000000E90400000000E70C0000000E0000000000000000E6040000000E2A020004E3100000000000000000000000000000000002020000EA04FFFFFFFF30011D2B0400000000207E')