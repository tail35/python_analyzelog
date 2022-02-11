#coding=utf-8
import os
import json
import urllib
import requests
import os.path
name="101289-5.log"
print (name)
num=0
livenum=0
myset=set()

file_json = open("my5.json", "a")
file_json.write("{\n")
file_json.write("\"RECORDS\": [\n")

with open(name,'r',encoding='utf-8') as file_obj:
    while 1:
        num=num+1
        lines = file_obj.readlines(10000)
        if not lines:
            break
        for line in lines: 
            oldline =line         
            pos = line.find("what_live")
            if(-1==pos):
                continue;
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
            #if "content" !="101289":
            #    continue
            mid = jsob['mid']
            livenum=livenum+1
            myset.add(mid)
            if(1==livenum):
                file_json.write(str(line))
            else:
                file_json.write(","+str(line))
            #print(mid)
            #print(num)

            
    file_obj.close()
print ("mysetnum:"+str(len(myset)))
print ("stanum: "+str(livenum))
file_json.write("]\n")
file_json.write("}\n")
file_json.close()
