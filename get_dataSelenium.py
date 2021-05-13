from selenium import webdriver
from time import sleep
import pandas as pd
from pandas import read_csv
from selenium.webdriver.common.keys import Keys

# 1.khai bao bien brower
brower = webdriver.Chrome(executable_path="./chromedriver.exe")# window 10
# brower = webdriver.Chrome(executable_path="./chromedriver")# linux
# 2.mo mot trang web
brower.get("https://diemthi.vnexpress.net/#area=2&college=undefined&q=score1")

data_sbd = []
data_tinh = []
data_toan = []
data_van = []
data_anh = []
data_su = []
data_dia = []
for i in range(1, 20):# lấy 5 tỉnh
	# Đợi trang web mở
	sleep(5)

	# click form chọn tỉnh
	local = brower.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/span/span[1]/span/span[2]')
	local.click()
	# điền form lấy từng tỉnh
	local = brower.find_element_by_xpath("/html/body/span/span/span[1]/input")
	ma_tinh = i
	ma_tinh = str(i)
	local.send_keys(ma_tinh)
	local.send_keys(Keys.ENTER)
	sleep(5)
	# get data
	data_ = brower.find_element_by_xpath('//*[@id="result"]/div[2]/div[2]/div/div[2]/div[3]/div/table/tbody')

	# xuất data -> csv

	data_ = data_.text
	print(data_)
	data_ = data_.split('\n')

	for data in data_:
		data = data.split(' ')
		while len(data)<13:
    			data.append('0')
		data_sbd.append(data[1])
		data_tinh.append(' '.join(data[2:6]))
		data_toan.append(data[6])
		data_van.append(data[7])
		data_anh.append(data[8])
		data_su.append(data[9])
		data_dia.append(data[10])

	hoc_sinh = {'sbd':data_sbd,
            	'tinh':data_tinh,
          		'toan':data_toan,
           		'van':data_van,
           		'anh':data_anh,
          		'su':data_su,
          		'dia':data_dia}

df = pd.DataFrame(hoc_sinh, columns = ['sbd', 'tinh','toan','van','anh','su','dia'])
df.to_csv(r'data.csv')

# 4.close brower
brower.close()
