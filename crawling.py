# 크롤링 라이브러리 import
#-*- coding:utf-8 -*-
import urllib
from importlib import reload

import requests
from bs4 import BeautifulSoup

#셀레니움
from selenium import webdriver

#오라클
#import os
#오라클 연동
#import cx_Oracle
#메모장출력
import sys

import time
import random


def hongmoon():
    driver=webdriver.Chrome('./chromedriver')

    driver.implicitly_wait(3)
    book_list=[]
    #http://www.gosisky.com/shop/goods/goods_list.php?&category=코드
    #005002 산업인력관리공단>토목
    #007 컴퓨터/IT
    count = 0
    classSet = ['01001', '01002', '01003', '01004', '01005', '01006', '01007', '01008', '01009', '02001', '02002', '02003', '02004', '02005', '02006', '03001', '03002', '03003', '03004', '03005', '03006', '03007', '04001', '04002', '04003', '04004', '04005', '04006']
    #,  에너지  '01007', 산업응용
    # 링크 위치 다른애들
    class1 = ['02001', '02002', '02003', '02004', '02005', '02006', '03001', '03002', '03003', '03004', '03005', '03006', '03007']
    #형식 다른애들
    class2 = ['01004', '01007', '01008']
    pageSet = []

    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005002")#토목
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005005")#건설
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005006")#환경
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005011")#에너지 - 형식다름
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005004")#전기
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005003")#기계
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005010")#산업응용 -형식다름
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005009")#위생 - 형식다름
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=005008")#기타
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=004010")#조리/미용 - 크롤링이 안됨
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=004027")#한국어능력
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=004026")#한자능력점정
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=004040")#공인
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=004041")#경제
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=004043")#운전
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006001")#toeic
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006002")#tofel
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006003")#teps
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006004")#opic
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006007")#중국어
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006009")#일본어
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=006006")#기타
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=007006")#프로그래밍
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=007004")#오피스
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=007005")#웹디자인
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=007002")#그래픽
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=007009")#컴퓨터 공학
    pageSet.append("http://www.gosisky.com/shop/goods/goods_list.php?&category=007008")#게임

    #print("pageSet : " + str(len(pageSet)) + "classSet : "+ str(len(classSet)))

    sys.stdout = open('output.txt', 'w')  # txt 파일로 print들 입력해서 출력하기

    errorPage = []
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=24818&category=005004")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=29163&category=007008")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=30161&category=005003")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=31547&category=005008")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=37408&category=004010005")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=36055&category=004010005")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=36670&category=006006004")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=31399&category=006006004")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=29693&category=006006004")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=37408&category=004010005")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=38122&category=005008")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=36670&category=006006004")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=29693&category=006006004")
    errorPage.append("http://www.gosisky.com/shop/goods/goods_view.php?goodsno=38111&category=007002")


    for homepage in pageSet :

        driver.get(homepage)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        total_page = 0#총페이지 수가 담길것

        for j in soup.select("body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.outline_side > div.indiv > form:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(1) > td > table:nth-child(2) > tbody > tr > td > div:nth-child(1) > a") :
            try :
                total_page = int(j.text[-3:-2])
            except :
                total_page =1

        if total_page == 0 :
            total_page = 9
        #print(total_page)


        #for j in soup.select("body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.outline_side > div.indiv > form:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(2) > td > table > tbody > tr > td > font:nth-child(2)") :
        #    print(j.text)


        for k in range(1, total_page+1) :
            #print(homepage+"&page="+str(k))
            driver.get(homepage+"&page="+str(k))
            #print("페이지 이동성공")
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            if classSet[count] in class1 :
                linkSelector = soup.select("body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.outline_side > div.indiv > form:nth-child(1) > table:nth-child(8) > tbody > tr:nth-child(5) > td > table > tbody > tr > td:nth-child(2) > div:nth-child(2) > a")
            elif classSet[count] in class2 :
                linkSelector = soup.select("body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.outline_side > div.indiv > form:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(5) > td > table > tbody > tr > td > table:nth-child(1) > tbody > tr > td > div > a")
            else :
                linkSelector = soup.select("body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.outline_side > div.indiv > form:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(5) > td > table > tbody > tr > td:nth-child(1) > div:nth-child(1) > a")

            for i in linkSelector :

                link = "http://www.gosisky.com/shop/" + i["href"][3:]
                #print(link)
                if link not in errorPage :
                    driver.get(link)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')

                    book = []


                    for j in soup.select("body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.outline_side > div.indiv > div:nth-child(2) > div:nth-child(2) > b") :
                        bookname= j.text.replace('\t', '').replace('\n', '').replace(',', '.')
                        book.append(bookname)
                        #print(book)


                    for j in soup.select("#goods_spec > form > table:nth-child(5) > tbody > tr:nth-child(3) > td") :
                        bookwriter= j.text.replace(",", "/")
                        book.append(bookwriter)
                        #print(book)

                    for j in soup.select("#goods_spec > form > table:nth-child(5) > tbody > tr:nth-child(2) > td") :
                        bookPublisher = j.text
                        book.append(bookPublisher)
                        #print(book)

                    for j in soup.select("#consumer"):
                        bookPrice = j.text.replace(",", "")
                        book.append(bookPrice)
                        #print(book)

                    for j in soup.select("#price > span:nth-child(1)"):
                        sale = j.text.replace(",", "")
                        book.append(sale)
                        #print(book)



                    for j in soup.select("#goods_spec > form > table:nth-child(5) > tbody > tr:nth-child(4) > td"):
                        publishDate = j.text
                        book.append(publishDate)
                        #print(book)


                    for j in soup.select("#goods_spec > form > table:nth-child(5) > tbody > tr:nth-child(5) > td"):
                        page = j.text.replace(",", "")
                        book.append(page)
                        #print(book)

                    for j in soup.select("#goods_spec > form > table:nth-child(5) > tbody > tr:nth-child(7) > td"):
                        ISBN = j.text
                        book.append(ISBN.strip())
                        book.append(classSet[count])
                        print(book)

                    for j in soup.select("#objImg"): #이미지 다운로드
                        img="http://www.gosisky.com/shop/" + j["src"][3:]
                        urllib.request.urlretrieve(img, "./image/"+ISBN + ".jpg")


                    #print(book)
                    book_list.append(book)
                    sys.stdout.flush()

                    driver.back()

        count = count + 1
        sys.stdout.flush()
    #print(book_list)
    return book_list