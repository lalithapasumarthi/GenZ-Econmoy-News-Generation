import sqlite3
import os
import requests
from bs4 import BeautifulSoup
import feedparser
import datetime
from time import sleep
from datetime import datetime

import os 
from groq import Groq
client = Groq(api_key='YOUR_API_KEY')

class database:
  def path():
    curr_directory = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(curr_directory, 'database_1.db')
    return db_path
  def db_create():
    file_path = database.path()
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    create_table = '''
                        create table if not exists entry(
                            id integer primary key,
                            time_stamp text,
                            link text,
                            post_original text,
                            title text,
                            post text
                        )
                        '''
    cursor.execute(create_table)
    conn.commit()
    conn.close()
  def db_select():
    file_path=database.path()
    conn= sqlite2.connect(file_path)
    cursor=conn.cursor()
    sql='select * from entry order by id desc'
    cursor.execute(sql)
    record=cursor.fetchall()
    conn.commit()
    conn.close()
    return record
  def db_check_record(link):
    file_path=database.path()
    conn = sqlite3.connect(file_path)
    cursor=conn.cursor()
    sql=f'select * from entry where link == "{link}"'
    cursor.execute(sql)
    record=cursor.fetchone()
    conn.commit()
    conn.close()
    return record
  def db_insert(link,post_original,title,post):
    time_stamp=datetime.now()
    file_path=database.path()
    conn=sqlite3.connect(file_path)
    cursor=conn.cursor()
    sql='insert into entry (time_stamp,link,post_original,title,post) values (?,?,?,?,?)'
    cursor.execute(sql,(time_stamp,link,post_original,title,post))
    conn.commit()
    conn.close()


def get_title(title):
  query=f''' -- {title}\
        -- give only one response\
        -- don not give any extra information\
        -- rewrite this title in GenZ slang\
        --dont include like here is rewriten etc and dont include Hindu businessline
        --add "\n"''' 
  chat_title=client.chat.completions.create(messages=[{
      "role":"user",
      "content": query
  }],model="llama3-8b-8192")
  return chat_title.choices[0].message.content

def get_blog(para):
  query=f''' -- {para}
        -- use this qive one response\
        -- don not give any extra information\
        -- rewrite this blog in GenZ slang in 200 words\
        --dont include like here is rewriten etc and dont include Hindu businessline '''
  chat_blog=client.chat.completions.create(messages=[{
      "role":"user",
      "content":query
  }],model="llama3-8b-8192")
  return chat_blog.choices[0].message.content

def parse(url):
  response=requests.get(url)
  soup=BeautifulSoup(response.text,'html.parser')
  title=soup.find('title').text
  ps=soup.find_all('p')
  para=""
  for p in ps:
    para='\n'.join([para,p.text])
  publish_time = soup.find('meta', {'property': 'article:published_time'})
  timestr=(publish_time.get('content'))
  return title,para

def collect_process():
  rss=['https://www.thehindubusinessline.com/economy/feeder/default.rss']
  for r in rss:
    feed=feedparser.parse(r)
    i=0
    for it in feed.entries:
      url=it['link']
      if database.db_check_record(url)==None:
        title,post_original=parse(url)
        title=get_title(title)
        words = post_original.split()
        post_original = ' '.join(words[:500])
        para=get_blog(post_original)
        post=""
        post_list=para.split('\n')
        for item in post_list:
          post=f'{post}<p>{item}</p>'
        print(f'POST ----{post}')
        database.db_insert(url,post_original,title,post)
        i+=1
        if(i>=10):
          break
      else:
        print("record already exists")

database.db_create()


os.system('clear')
collect_process()
sleep(100)