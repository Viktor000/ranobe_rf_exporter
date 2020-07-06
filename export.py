#!/usr/bin/python3
 
import urllib.request
import json
#url='https://xn--80ac9aeh6f.xn--p1ai/vlasty-knighnogo-chervya'
url='https://xn--80ac9aeh6f.xn--p1ai/uchenik-karty'
count=0


name=url[url.rfind("/")+1:len(url)]
url2="https://xn--80ac9aeh6f.xn--p1ai/api/v2/books/" + name + "/chapters"
html_doc = urllib.request.urlopen(url2).read()          
chapters=json.loads(html_doc)
url3="https://xn--80ac9aeh6f.xn--p1ai/api/v2/books/" + name
html_doc = urllib.request.urlopen(url3).read()          
book=json.loads(html_doc)                

book_title= book.get("title")
book_description=book.get("description")
genres=""

for i in range(len(book.get("genres"))):
    genres+="\n<genre>" + book.get("genres")[i].get("title")+"</genre>"

data2=chapters.get("items")
data2.reverse()
dat_title={}
dat_url={}
with open("fb2_templ.fb2", "r") as read_file:
            templ=read_file.read()

for i in range(len(data2)):
    templ2=templ
    data_temp=dict(data2[i])
    dat_title[i]=data_temp.get("title")
    dat_url[i]= url2 +"/"+ data_temp.get("slug") 


text_str=""
print (len(dat_url))
#for i in range(len(dat_url)):
while (count<len(dat_url)):
        #print(dat_url.get(i))
        print ("Part №" + str(count) +" Start")
        html_doc2 = urllib.request.urlopen(dat_url.get(count)).read()          
        glava=json.loads(html_doc2)
        text=glava.get("text")
        if isinstance(text.get("text"), str):
            title=glava.get("title")
            text_str+="\n<title>" + title + "</title>\n"
            text_str+= text.get("text")
        count+=1
part=templ2.replace("{title}",book_title)
part=part.replace("{description}",book_description)
part=part.replace("{genres}",genres)
part=part.replace("{text}",text_str)


with open(book_title+".fb2", "w") as write_file1:
    write_file1.write(part)
print ("Finish")