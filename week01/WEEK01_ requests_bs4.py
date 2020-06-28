import requests
from bs4 import BeautifulSoup
import pandas as pd


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
cookie = '__mta=146093323.1593155858665.1593155858665.1593155858665.1; uuid_n_v=v1; uuid=19867A60B77D11EA80F64D80EBA969F7C3E68C703C4040DABDF812650E9362A0; _lxsdk_cuid=172ef7d2135c8-05803e2c153f38-5393662-1fa400-172ef7d2135c8; _lxsdk=19867A60B77D11EA80F64D80EBA969F7C3E68C703C4040DABDF812650E9362A0; mojo-uuid=e72afee03901fbe1814189b729a55d77; _csrf=a163896e35d9a3f03b6689eadd21c346f4fdd3cee1e9a2c63aaf527d680aaf6a; lt=6-X5641FG0doI0DUHcTDRAsGMV4AAAAA5woAAA6RaWZShqBPn6Tpl8LRTMcneT2kZqUqvIARgjLYVBERlri1imMN8QpWjWCUm9Q72Q; lt.sig=Kblxuoklrqz2eo0bI_ucjOp8IJY; mojo-session-id={"id":"5a4298124ad654790feb14bfd288d871","time":1593165858381}; mojo-trace-id=8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593165858,1593166511,1593166528,1593166539; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593166539; __mta=146093323.1593155858665.1593155858665.1593166539119.2; _lxsdk_s=172f015c66d-fb4-b1a-06c%7C%7C12'

header = {'user-agent':user_agent,'cookie':cookie}
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl,headers=header)


bs = BeautifulSoup(response.text, 'html.parser')
dic_item = {
    '电影名称': [],
    '电影类型': [],
    '上映时间': []
}

limit = 10
n = 0
for tags in bs.find_all('div', attrs={'class': 'movie-hover-info'}):
    if n >= 10:
        break

    for tags2 in tags.find_all('div', ):
        if tags2.find('span', attrs={'class': 'name'}) is not None:
            name = tags2.find('span', attrs={'class': 'name'}).text
            dic_item['电影名称'].append(name)
         
        elif tags2.find('span', ).text[:-1] == '类型':
            mold = tags2.text.split('\n')[2].strip()
            dic_item['电影类型'].append(mold)
      
        elif tags2.find('span', ).text[:-1] == '上映时间':
            release_time = tags2.text.split('\n')[2].strip()
            dic_item['上映时间'].append(release_time)

    n += 1
  
pd.DataFrame(dic_item).to_csv('requests_bs4_猫眼电影前10.csv', encoding='utf-8-sig')
