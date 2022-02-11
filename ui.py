#coding=utf-8
import os
import json
import urllib
import requests
import os.path
import codecs
name="101289-1.log"
print (name)
num=0
livenum=0
myset=set()

file_json = codecs.open("ui1.json","a","utf-8")
file_json.write("{\n")
file_json.write("\"RECORDS\": [\n")

with open(name,'r',encoding='utf-8') as file_obj:
#with open(name,'r',encoding='gb2312') as file_obj:
    while 1:
        lines = file_obj.readlines(10000)
        if not lines:
            break
        for line in lines: 
            num+=1
            oldline =line                     
            pos = line.find("what_live")
            if(-1!=pos):
                continue;            
            pos = line.find("101289")
            if(-1==pos):
                continue; 
            # pos = line.find("143_wmgkk_h5_zbj_00025")
            # if(-1==pos):
            #     continue;                
            line=line.replace("\\\\\\","___")
            line=line.replace("\\","")            
            line=line.replace("___","\\")

            line=line.replace("\\\"","___")
            line=line.replace("\\","\\\\")
            line=line.replace("___","\\\"")            
            try:
                jsob = json.loads(line)  
                #print(line)
            except Exception:                
                print(line)
                continue
                #print(oldline)
            #print(line)
            #if "event_time" not in jsob:
            #    continue            
            #if "content" not in jsob:
            #    continue
            if "mid" not in jsob:
                print("nomid:"+str(line))
                continue
            mid = jsob['mid']
            
            
            livenum+=1

            myset.add(mid)
            if(1==livenum):
                file_json.write(str(line))
            else:
                file_json.write(","+str(line))
            #print(mid)
            #print(num)

            if(2==livenum):
                break

            
    file_obj.close()
print ("mysetnum:"+str(len(myset)))
print ("livenum: "+str(livenum))
file_json.write("]\n")
file_json.write("}\n")
file_json.close()
