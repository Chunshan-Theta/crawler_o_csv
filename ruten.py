#coding:utf-8
import csv
from selenium import webdriver


def FindAllElementsByClass(driver,className,show=0):
	# "find_elements_by_class_name"return all element
	# "find_element_by_class_name"return first element
	content = driver.find_elements_by_class_name(className)
	if show:
		for i in content:
			print i.text
	return content

result = []
for i in range(2):
	driver = webdriver.Chrome()
	# 輸入範例網址，交給瀏覽器
	driver.get('http://class.ruten.com.tw/user/index00.php?s=sunny22ya&p='+str(i+1))   

	# 取得網頁原始碼
	#pageSource = driver.page_source  

	price = FindAllElementsByClass(driver,"item-direct-price")
	name = FindAllElementsByClass(driver,"item-name")
	
	for index in range(len(name)):
		unit = []
		unit.append(price[index].text[7:len(price[index].text)-2])
		unit.append(name[index].text[8:].encode('utf-8'))
		result.append(unit)
		#print price[index].text[7:len(price[index].text)-2],name[index].text[8:]
	driver.close()  # 關閉瀏覽器


f = open("ruten.csv","a")
w = csv.writer(f)
w.writerows(result)
f.close()


