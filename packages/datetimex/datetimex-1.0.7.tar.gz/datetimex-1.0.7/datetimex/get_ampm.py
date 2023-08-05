from datetimex.log import d as log

def gettime_ampm(text,time_now):
	ampm = ''
	am_list = ['上午','凌晨','早上','早晨','晨']
	pm_list = ['下午','中午','晚上','傍晚','深夜','夜晚','晚']
	for x in am_list:							##这里把两个数组给予遍历，用作当两个数组都没有的情况异常可控
		if x in text:	
			ampm = 'am'
	for x in pm_list:
		if x in text:
			ampm = 'pm'							##这里将ampm赋值为小写，规定为后续格式化时间时，小写代表不可进行修改，直接使用该数据
	if ampm == '':
		ampm = time_now[11:13]
	return str(ampm)
		

def main(list,text,time_now):
	ampm = gettime_ampm(text,time_now)
	return ampm