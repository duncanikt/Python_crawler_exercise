import requests
from bs4 import BeautifulSoup

# 目標網頁的 URL
url = 'https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

# 發送 HTTP 請求，獲取網頁內容
response = requests.get(url)

# 使用 BeautifulSoup 解析 HTML 內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到網頁中的所有 h1 到 h6 標籤
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# 印出每個標籤的文字內容
for index, heading in enumerate(headings, start=1):
    print(f'標題 {index}: {heading.text}')

# 如果找不到任何標題，印出提示訊息
if not headings:
    print('找不到任何標題')
