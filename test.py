from pyquery import PyQuery as pq
import requests
import codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17',
    'Set-Cookie':'MasterSymbol=03333;'
}
r = requests.get("http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=03333.HK", headers, timeout=10)
#d = pq('http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=03333')
d = pq(r.text)
print(d.html())
# print(d("tbQuote").find('#labelLast').text())

# from selenium import webdriver
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# driver = webdriver.Firefox()
# driver.get("http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=03333")
# #q = driver.find_element_by_id("cp_pLeft")
# print(driver)