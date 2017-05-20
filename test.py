from pyquery import PyQuery as pq
import requests
import codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

headers = {
    'Host': 'www.aastocks.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.29 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer' : 'http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=03333',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cookie':'ASP.NET_SessionId=2tgojfckdt3twhq1hhl1htkn; MasterSymbol=03333; LatestRTQuotedStocks=03333; aa_cookie=61.10.70.173_56647_1495131731; AALTP=1'
}
r = requests.get("http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=03333", headers)
d=pq(r.text)
print("txtHKQuote"+d("#txtHKQuote").val())
print(d('#cp_pErrMsg').html())
print(r.history)


