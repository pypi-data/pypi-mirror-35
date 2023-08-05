import os
from tqdm import tqdm
import re
import requests
def nas_fetch_it(url,save_path,file_type):
    save_path = str(save_path)
    if(save_path[-1] != "/"):
        save_path = save_path + "/"
    save_path = save_path.replace("\\","/")
    file_type = file_type.replace("*","").replace(".","")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    re_files = re.findall('"((http|ftp)s?://.*?)"', html)
    var=0
    if(len(re_files) == 0):
        re_files = re.findall('"(('+file_type+')s?://.*?)"', html)
    if(len(re_files) == 0):
        re_files = re.findall('href=[\'"]?([^\'" >]+)', html)
        var=1
    files = []
    if(var == 0):
        for _ in re_files:
            files.append(_[0])
    else:
        for _ in re_files:
            files.append(_)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    mp3_files = []
    for _ in files:
        if(file_type not in _):
            pass
        else:
            mp3_files.append(_)
    assert (len(mp3_files) != 0) , "No File Found"
    actual_urls = []
    for _ in  mp3_files:
        if("https:" in _):
            temp_url = str(str(str("https://"+str(_.split("https://")[1])).split(file_type)[0])+file_type)
        elif("http:" in _):
            temp_url = str(str(str("http://"+str(_.split("http://")[1])).split(file_type)[0])+file_type)
        elif("www." in _):
            temp_url = str(str(str("www."+str(_.split("www.")[1])).split(file_type)[0])+file_type)
        elif(".com" in _):
            temp_url = str(str(str("'"+str(_.split("'")[1])).split(file_type)[0])+file_type)
        else:
            if(url[-1] == "/"):
                temp_url = str(url+str(_))
            else:
                temp_url = str(url+"/"+str(_))
        actual_urls.append(temp_url)
    assert (len(actual_urls) != 0) , "No File Found"
    actual_urls = list(set(actual_urls))
    for _ in tqdm(range(len(actual_urls))):
        #print(_ , "Done")
        #wget.download(actual_urls[_],str(save_path+str(_)+".mp3"))
        #print(str(save_path+str(os.path.basename(actual_urls[_]))))
        r = requests.get(actual_urls[_])
        with open(str(save_path+str(os.path.basename(actual_urls[_]))),'wb') as f:
            f.write(r.content)
