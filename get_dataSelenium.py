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
data_ly = []
data_hoa = []
data_sinh = []
data_su = []
data_dia = []
data_gdcd = []

for i in range(1, 65):# lấy 63 tỉnh

<<<<<<< HEAD
	# xuất data -> csv
=======
    # fix loi du lieu
    if i == 20:
        continue
>>>>>>> 72cd80cb678258e88e741cc6a5d6f2f2592d198c

    # Đợi trang web mở
    sleep(5)

<<<<<<< HEAD
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
=======
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
>>>>>>> 72cd80cb678258e88e741cc6a5d6f2f2592d198c


    for r in range(2, 101):
        data = []
        for c in range(1, 15):
            temp = brower.find_element_by_xpath('//*[@id="result"]/div[2]/div[2]/div/div[2]/div[3]/div/table/tbody/tr['+str(r)+']/td['+str(c)+']').text
            if (temp == ""):
                temp = "0"
            data.append(temp)
        # luu tru data
        print(data)
        data_sbd.append(data[1])
        data_tinh.append(data[2])
        data_toan.append(data[3])
        data_van.append(data[4])
        data_anh.append(data[5])
        data_ly.append(data[7])
        data_hoa.append(data[8])
        data_sinh.append(data[9])
        data_su.append(data[11])
        data_dia.append(data[12])
        data_gdcd.append(data[13])

# 4.close brower
brower.close()

#   xuat data
# tao file data.csv
f = open('data.csv', 'w')

hoc_sinh = {'sbd':data_sbd,
            'tinh':data_tinh,
          	'toan':data_toan,
           	'van':data_van,
           	'anh':data_anh,
            'ly':data_ly,
            'hoa':data_hoa,
            'sinh':data_sinh,
          	'su':data_su,
          	'dia':data_dia,
            'gdcd':data_gdcd}

df = pd.DataFrame(hoc_sinh, columns = ['sbd', 'tinh','toan','van','anh','ly','hoa','sinh','su','dia','gdcd'])
df.to_csv(r'data.csv')
