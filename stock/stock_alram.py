# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:44:33 2021

@author: kim-eungyeong
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from bs4 import BeautifulSoup
import urllib.request as req
import requests


font_size = 8
url = 'https://finance.daum.net/quotes/A093230#home'
res=req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')



def check_price():
    codes = ['093230'] # 종목코드 리스트
    for code in codes:
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
    
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    
        today = soup.select_one('#chart_area > div.rate_info > div')
        price = today.select_one('.blind')
        prices = price.get_text()
    
    return prices

def check_name():
    codes = ['093230'] # 종목코드 리스트
    for code in codes:
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
    
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    
        name = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
    
    return name
        
################################################################################
# 윈도우 창에 프로그램을 띄워줄 프로그램 
################################################################################
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('stock_alram')
        
################################################################################
# 숫자, 연산자 입력시 출력되는 라벨창
################################################################################


# title
title1 = QLabel()
title2 = QLabel()

#font
font1 = title1.font()
font1.setPointSize(font_size)

title1.setFont(font1)
title2.setFont(font1)

title1.setText("이름")
title2.setText("현재가")


#종목 이름
name = QLabel()
name.setAlignment(Qt.AlignCenter)
name.setFont(font1)

#현재가
price = QLabel()
price.setFont(font1)

name.setText(check_name())
price.setText(check_price())


################################################################################
# 화면 레이아웃 구성
################################################################################
layout_main = QVBoxLayout()
layout_sub1 = QGridLayout()

layout_sub1.addWidget(title1, 0, 0)
layout_sub1.addWidget(title2, 0, 1)
layout_sub1.addWidget(name, 1, 0)
layout_sub1.addWidget(price, 1, 1)

################################################################################
# 버튼
################################################################################
btn1 = QPushButton('1')

################################################################################
# 버튼과 함수 연결
################################################################################
'''
btn1.clicked.connect(pushbtn1)
'''

################################################################################
# 버튼 레이아웃 설정
################################################################################
#layout_sub1.addWidget(btn1, 1, 2)
'''
layout_sub1.addWidget(btn2, 0, 1)
'''

################################################################################
# 메인레이아웃에 버튼 레이아웃 추가
################################################################################
layout_main.addLayout(layout_sub1)


################################################################################
# 출력
################################################################################
window.setLayout(layout_main)
window.show()
sys.exit(app.exec_())
