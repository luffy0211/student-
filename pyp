import  requests
from selenium import webdriver
import time
#定义解析函数
def parse(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    #循环控制
    flag = True
    num=10
    while flag:
        #每执行一次循环，num减1
        num = num-1
        print('正在解析第'+str(10-num) +'页')



        #电影名称
        movie_name = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
        #电影时间
        movie_time = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[3]')

        for i in range(len(movie_name)):
            movie_name=movie_name[i].text
            movie_time=movie_time[i].text.split('：')[1]
            print('电影名称：',movie_name)
            print('上映时间：',movie_time)
            yield {
                '电影名称':movie_name,
                '上映时间':movie_time
            }
        #
        time.sleep(3)
        #判断能否点击下一页
        if num >0:
            #点击下一页
            next_page = driver.find_elements_by_link_text('下一页')
            next_page.click()
            #显示等待
            driver.implicitly_wait(10)
        else:
            flag = False

def save_data():
    with open('猫眼电影.txt','w',encoding='utf-8') as f:
        url = 'https://www.maoyan.com/board/4?timeStamp=1714448532417&channelId=40011&index=2&signKey=a95e203f0c3b605e8f77df3f2e2a8c65&sVersion=1&webdriver=false'
        for movie_dict in parse(url):
            f.write(str(movie_dict)+'\n')

if __name__ == '__main__':
    save_data()
