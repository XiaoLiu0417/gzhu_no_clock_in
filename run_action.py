from login_new import login_new
from clock_in import clock_in
import os
import requests

stu_id = str(os.environ['STUID'])
pwd = str(os.environ['STUPWD'])

res = requests.get("https://gzhu.edu.cn")
print(res.content)

login_new(stu_id, pwd)
clock_in(stu_id)
