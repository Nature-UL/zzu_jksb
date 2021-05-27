import re
import requests

#账号 密码
id = "XXXX"
pwd = "XXXX"

#login
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',	
	'referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0?fun2=a',
	'Content-Type':'application/x-www-form-urlencoded'
}
form={
	"uid": id,
	"upw": pwd,
	"smbtn": "进入健康状况上报平台",
	"hh28": "750"  #按照当前浏览器窗口大小计算
}
r= requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login",headers=headers,data=form) #response为账号密码对应的ptopid和sid信息

text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
#first6
matchObj = re.search(r'ptopid=(\w+)\&sid=(\w+)\"',text)
ptopid = matchObj.group(1) 
sid = matchObj.group(2) 
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',	
	'referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
}
r = requests.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid="+ptopid+"&sid="+sid+"&fun2=") #response里含有jksb对应的params

text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
#jksb?with_params 
matchObj = re.search(r'ptopid=(\w+)\&sid=(\w+)\&',text)
ptopid = matchObj.group(1) 
sid = matchObj.group(2) 
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',	
	'referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
}
r = requests.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid="+ptopid+"&sid="+sid+"&fun2=",headers=headers) #response为jksb表单第一页
ptopid1 = ptopid
sid1 = sid

text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
#DONE
matchObj = re.search(r'name=\"ptopid\" value=\"(\w+)\".+name=\"sid\" value=\"(\w+)\".+',text)
ptopid = matchObj.group(1) 
sid = matchObj.group(2) 
form = {
	"day6": "b",
	"did": "1",
	"door": "",
	"men6": "a",
	"ptopid": ptopid,
	"sid": sid
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
	'Referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid='+ptopid1+'&sid='+sid1+'&fun2=',
    'Content-Type':'application/x-www-form-urlencoded'
}
r = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb",headers=headers,data=form) #response为打卡的第二个表单

text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
#DONE
matchObj = re.search(r'name=\"ptopid\" value=\"(\w+)\".+name=\"sid\" value=\"(\w+)\"',text)
ptopid = matchObj.group(1) 
sid = matchObj.group(2) 
form = {
	"myvs_1": "否",
	"myvs_2": "否",
	"myvs_3": "否",
	"myvs_4": "否",
	"myvs_5": "否",
	"myvs_6": "否",
	"myvs_7": "否",
	"myvs_8": "否",
	"myvs_9": "否",
	"myvs_10": "否",
	"myvs_11": "否",
	"myvs_12": "否",
	"myvs_13a": "41",
	"myvs_13b": "4101",
	"myvs_13c": "河南省.郑州市.科学大道100号",
	"myvs_14": "否",
	"myvs_14b": "",
	"memo22": "[待定]",
	"did": "2",
	"door": "",
	"day6": "b",
	"men6": "a",
	"sheng6": "",
	"shi6": "",
	"fun3": "",
	"jingdu": "0.0000",
	"weidu": "0.0000",
	"ptopid": ptopid,
	"sid": sid
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
	'Referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb',
	'Content-Type':'application/x-www-form-urlencoded'
}
r = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb",data=form,headers=headers) #response为完成打卡页面
text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
if("感谢你今日上报健康状况！" in text):
    print("打卡成功")
else:
    print("打卡失败")

   

