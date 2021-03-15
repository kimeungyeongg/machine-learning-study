# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:44:33 2021

@author: kim-eungyeong
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt
from bs4 import BeautifulSoup
import urllib.request as req
import requests


codes = ['093230', '005930', '000660', '003490', '035720'] # 종목코드 리스트
font_size = 8
url = 'https://finance.daum.net/quotes/A093230#home'
res=req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')


def check_price(codes= list):
    prices = list()
    for code in codes:
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
    
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    
        today = soup.select_one('#chart_area > div.rate_info > div')
        price = today.select_one('.blind')
        #prices = price.get_text()
        prices.append(price.get_text())
    
    price1.setText(prices[0])
    price2.setText(prices[1])
    price3.setText(prices[2])
    price4.setText(prices[3])
    price5.setText(prices[4])

def check_name(codes= list):
    names = list()
    for code in codes:
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
    
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')    
        name = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
        names.append(name)
        
    name1.setText(names[0])
    name2.setText(names[1])
    name3.setText(names[2])
    name4.setText(names[3])
    name5.setText(names[4])
  
def btnclick():
    global codes
    codes[:] = []    
    codes = textbox.text().split(",")
    print(codes)
    check_name(codes)
    check_price(codes)
    
################################################################################
# 윈도우 창에 프로그램을 띄워줄 프로그램 
################################################################################
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('stock_alram')
        
################################################################################
# 숫자, 연산자 입력시 출력되는 라벨창
################################################################################
textbox = QLineEdit()
textbtn = QPushButton('check')
textbtn.clicked.connect(btnclick)

# title
title1 = QLabel()
title2 = QLabel()
title1.setAlignment(Qt.AlignCenter)
title2.setAlignment(Qt.AlignCenter)

#font
font1 = title1.font()
font1.setPointSize(font_size)

title1.setFont(font1)
title2.setFont(font1)

title1.setText("이름")
title2.setText("현재가")


#종목 이름
name1 = QLabel()
name2 = QLabel()
name3 = QLabel()
name4 = QLabel()
name5 = QLabel()
name1.setAlignment(Qt.AlignCenter)
name2.setAlignment(Qt.AlignCenter)
name3.setAlignment(Qt.AlignCenter)
name4.setAlignment(Qt.AlignCenter)
name5.setAlignment(Qt.AlignCenter)
name1.setFont(font1)
name2.setFont(font1)
name3.setFont(font1)
name4.setFont(font1)
name5.setFont(font1)

#현재가
price1 = QLabel()
price2 = QLabel()
price3 = QLabel()
price4 = QLabel()
price5 = QLabel()
price1.setAlignment(Qt.AlignCenter)
price2.setAlignment(Qt.AlignCenter)
price3.setAlignment(Qt.AlignCenter)
price4.setAlignment(Qt.AlignCenter)
price5.setAlignment(Qt.AlignCenter)
price1.setFont(font1)
price2.setFont(font1)
price3.setFont(font1)
price4.setFont(font1)
price5.setFont(font1)

check_name(codes)
check_price(codes)
################################################################################
# 화면 레이아웃 구성
################################################################################
layout_main = QVBoxLayout()
layout_textbox = QHBoxLayout()
layout_sub1 = QVBoxLayout()
layout_list = QGridLayout()

layout_textbox.addWidget(textbox)
layout_textbox.addWidget(textbtn)

layout_list.addWidget(title1, 0, 0)
layout_list.addWidget(title2, 0, 1)
layout_list.addWidget(name1, 1, 0)
layout_list.addWidget(name2, 2, 0)
layout_list.addWidget(name3, 3, 0)
layout_list.addWidget(name4, 4, 0)
layout_list.addWidget(name5, 5, 0)
layout_list.addWidget(price1, 1, 1)
layout_list.addWidget(price2, 2, 1)
layout_list.addWidget(price3, 3, 1)
layout_list.addWidget(price4, 4, 1)
layout_list.addWidget(price5, 5, 1)

################################################################################
# 버튼과 함수 연결
################################################################################
'''
btn1.clicked.connect(pushbtn1)
'''

################################################################################
# 버튼 레이아웃 설정
################################################################################
#layout_sub2.addWidget(btn1, 1, 2)
'''
layout_sub2.addWidget(btn2, 0, 1)
'''

################################################################################
# 메인레이아웃에 버튼 레이아웃 추가
################################################################################

layout_sub1.addLayout(layout_textbox)
layout_sub1.addLayout(layout_list)
layout_main.addLayout(layout_sub1)


################################################################################
# 출력
################################################################################
window.setLayout(layout_main)
window.show()
sys.exit(app.exec_())
