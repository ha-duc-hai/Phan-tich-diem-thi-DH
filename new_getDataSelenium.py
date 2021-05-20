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

# tao file data.csv
hoc_sinh = ['sbd','tinh','toan','van','anh','ly','hoa','sinh','su','dia','gdcd']

try:
    df = read_csv('new_data.csv')
except:
    df = pd.DataFrame(columns = hoc_sinh)
    df = df.to_csv('new_data.csv')

stt = 71
ma_tinh = 4
stt_temp = stt
ma_tinh_temp = ma_tinh
while (stt < 501 and ma_tinh < 65):
    try:
        for i in range(ma_tinh, 65):# lấy mã tỉnh
            ma_tinh_temp = i
            if (stt_temp >= 500):
                stt = 1
            # fix lỗi dữ liệu
            if i==20:
                continue

<<<<<<< HEAD
            sleep(5) #đợi load trang
            # tạo mã id
            id_ = str(i)
            if i < 10:
                id_ = '0' + id_

            for num in range(stt, 501):# lấy 1000 dl của mỗi tỉnh
                stt_temp = num
                _id = str(num)
                while len(_id) < 6:
                    _id = '0' + _id

                id = id_ + _id
                # click và điền form
                input = brower.find_element_by_xpath('//*[@id="keyword"]')
                input.send_keys(id)
                input.send_keys(Keys.ENTER)
                sleep(2)
                data = []
                for c in range(1,15):
                    temp = brower.find_element_by_xpath('//*[@id="result"]/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td['+str(c)+']').text
                    if (temp == ""):
                        temp = "0"
                    data.append(temp)
                # tách dl cần lấy 
                data_temp = []
                data_temp.append(data[1])
                data_temp.append(data[2])
                data_temp.append(data[3])
                data_temp.append(data[4])
                data_temp.append(data[5])
                data_temp.append(data[7])
                data_temp.append(data[8])
                data_temp.append(data[9])
                data_temp.append(data[11])
                data_temp.append(data[12])
                data_temp.append(data[13])
                # update dữ liệu vào csv
                df_temp= pd.DataFrame([data_temp], columns=hoc_sinh)
                df_temp.to_csv('new_data.csv', mode='a', header=False)
    except:
        ma_tinh = ma_tinh_temp
        stt = stt_temp + 1
=======
    sleep(2) #đợi load trang
    # tạo mã id
    id_ = str(i)
    if i < 10:
        id_ = '0' + id_

    for num in range(410, 501):# lấy 1000 dl của mỗi tỉnh
        _id = str(num)
        while len(_id) < 6:
            _id = '0' + _id

        id = id_ + _id
        # click và điền form
        input = brower.find_element_by_xpath('//*[@id="keyword"]')
        input.send_keys(id)
        input.send_keys(Keys.ENTER)
        sleep(2)
        data = []
        for c in range(1,15):
            temp = brower.find_element_by_xpath('//*[@id="result"]/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td['+str(c)+']').text
            if (temp == ""):
                temp = "0"
            data.append(temp)
        # tách dl cần lấy
        data_temp = []
        data_temp.append(data[1])
        data_temp.append(data[2])
        data_temp.append(data[3])
        data_temp.append(data[4])
        data_temp.append(data[5])
        data_temp.append(data[7])
        data_temp.append(data[8])
        data_temp.append(data[9])
        data_temp.append(data[11])
        data_temp.append(data[12])
        data_temp.append(data[13])
        # update dữ liệu vào csv
        df_temp= pd.DataFrame([data_temp], columns=hoc_sinh)
        df_temp.to_csv('new_data.csv', mode='a', header=False)

>>>>>>> e60805c86e5a3cb75ec66fd7f554bc6c867050bd
# đóng trình duyệt
brower.close()

