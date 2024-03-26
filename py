import re
import requests
import random
url='https://www.maoyan.com/board/4?timeStamp=1711415298865&channelId=40011&index=3' \
    '&signKey=2ae4eeb9bd6d397dc32c19bfb1d6b9e4&sVersion=1&webdriver=false&offset=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36'
}
def random_num(n):
    random_num=random.sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789',n)
    return ''.join(random_num)
code = random_num(37)
for i in range(10):
    url = 'https://www.maoyan.com/board/4?offset=' + str(i*10) + '&requestCode=' + code
    response = requests.get(url,headers=headers)
    html = response.text
    print(html)
