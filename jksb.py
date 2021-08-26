#账号 密码
id = "XXXX"
pwd = "XXXX"  
#账号和密码需要被双引号""包裹
#   eg:
#       id = "201988880101"
#       pwd = "password"

import re
import requests
import json #用于读取账号信息
import time #用于计时重新发送requests请求
import base64 #用于解密编码
import logging #用于日志控制
import os,sys


curr_dir = os.path.dirname(os.path.abspath(__file__))
r=""

#set logging format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
#create a log file at the work directory
logging.basicConfig(filename=curr_dir+'/my.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.info("===开始打卡===")

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
r = ""
max_punch = 10
curr_punch = 0 #if curr_punch > max_pubch then exit
logging.info("准备进入打卡界面")
while True:
    try:
        logging.info("准备进入post请求")
        r= requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login",headers=headers,data=form,timeout=(200,200)) #response为账号密码对应的ptopid和sid信息,timeout=60(sec)
        logging.info("成功运行post请求")
    except:
        logging.warning("请检查网络链接是否正常")
        curr_punch+=1
        if curr_punch>max_punch:
            exit()
        time.sleep(120)     #sleep 60 sec
    else:
        break
text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
r.close()
del(r)
#first6
matchObj = re.search(r'ptopid=(\w+)\&sid=(\w+)\"',text)
try:
    ptopid = matchObj.group(1) 
    sid = matchObj.group(2) 
except:
    logging.warning("请检查账号"+id+"和密码"+pwd+"是否正确，或检查是否有验证码")
    exit()
else:
    logging.info("账号密码正确")
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',	
    'referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
}
curr_punch=0
while True:
    try:
        r = requests.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid="+ptopid+"&sid="+sid+"&fun2=") #response里含有jksb对应的params
    except:
        logging.error("get请求失败")
        if curr_punch>max_punch:
            exit()
        curr_punch+=1
        time.sleep(120)
    else:
        break
text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
r.close()
del(r)
#jksb?with_params 
matchObj = re.search(r'ptopid=(\w+)\&sid=(\w+)\&',text)
ptopid = matchObj.group(1) 
sid = matchObj.group(2) 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',	
    'referer':'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
}
curr_punch=0
while True:
    try:
        r = requests.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid="+ptopid+"&sid="+sid+"&fun2=",headers=headers) #response为jksb表单第一页
    except:
        logging.info("第二次get请求失败")
        while curr_punch>max_punch:
            exit()
        curr_punch+=1
        time.sleep(120)
    else:
        break
ptopid1 = ptopid
sid1 = sid

text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
r.close()
del(r)
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
while True:
    try:
        r = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb",headers=headers,data=form) #response为打卡的第二个表单
    except:
        while curr_punch>max_punch:
            exit()
        curr_punch+=1
    else:
        break
text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
r.close()
del(r)
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
    "myvs_13": "g",
    "myvs_13a": "41",
    "myvs_13b": "4101",
    "myvs_13c": "河南省.郑州市.科学大道100号",
    "myvs_24": "否",
    "myvs_14b": "",#已弃用
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
while True:
    try:
        r = requests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb",data=form,headers=headers) #response为完成打卡页面
    except:
        while curr_punch>max_punch:
            exit()
        curr_punch+=1
    else:
        break
text = r.text.encode(r.encoding).decode(r.apparent_encoding) #解决乱码问题
r.close()
del(r)
if("感谢你今日上报健康状况！" in text):
    logging.info(id+":打卡成功")
    print(id+":打卡成功")
else:
    logging.info(id+":打卡失败")
    print(id+":打卡失败")
   

