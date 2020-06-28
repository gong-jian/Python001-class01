import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

'''
抓取猫眼top电影信息
request获取页面内容，BeautifulSoup解析页面内容，用pandas将结果保存到csv文件中
'''
# 电影名称、电影类型和上映时间
#猫眼top页面链接
url = 'https://maoyan.com/films?showType=3'
#访问页面客户端
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# 猫眼电影首次进入会跳转美团验证页面，在浏览器中验证后将cookie复制到这里
COOKIE = 'uuid_n_v=v1; uuid=C9DC78C0B5EC11EAA1F189776DB49E05E5738CACDADE4974A02CC499DA916529; _csrf=d8595a669bf88499438c27cfee9ced7f638222b687994aebc831323b6b0bb79a; _lxsdk_cuid=172e53d9e8b48-03f090d8d3be3d-4353760-240000-172e53d9e8cc8; _lxsdk=C9DC78C0B5EC11EAA1F189776DB49E05E5738CACDADE4974A02CC499DA916529; mojo-uuid=3d3033e3315c555f41796e8c3e5607ab; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592983920,1592983939,1592984076; mojo-session-id={"id":"9f05796af0806090a150b4f96d7c567a","time":1592986323738}; mojo-trace-id=9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592988094; __mta=213163691.1592983920571.1592988077505.1592988094254.13; _lxsdk_s=172e53d9e8d-6c3-852-7a8%7C%7C36'

myList = []

def get_url_name(myurl, num):
    header = {'User-Agent': USER_AGENT, 'Cookie': COOKIE}
    response = requests.get(url=myurl, headers=header)
    # print(response)
    bs_info = bs(response.text, 'html.parser')
    #print(bs_info)

    for i, tags in enumerate(bs_info.find_all('div', attrs={'class': 'movie-hover-info'})):
        if i >= num:
            break
        movie_list = []
        for tag in tags.find_all('div'):
            span = tag.find('span')
            print(span.attrs['class'][0].strip())
            if span.attrs['class'][0].strip() == 'name':
                movie_name = span.text.strip()
                movie_list.append(movie_name)
            if span.text == '类型:':
                movie_type = tag.text.split()[-1]
                movie_list.append(movie_type)
            if span.text == '上映时间:':
                movie_time =tag.text.split()[-1]
                movie_list.append(movie_time)
        myList.append(movie_list)
    
get_url_name(url,10)
result_data = pd.DataFrame(myList)
result_data.to_csv('./requests_bs4_resutl.csv',encoding='utf8', index=False, header=False)