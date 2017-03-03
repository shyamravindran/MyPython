import json
 

with open('chetan.json',"r") as dataf:
        data = json.load(dataf)

print type(data)
fle = open('cheta.txt', 'w')
for i in data:
	if i.get("port") == None:
		fle.write(i["tag"][0]+"."+i["tag"][1]+"."+i["tag"][2]+"   "+i["usernam"]+"@"+i["domain"])
        elif i.get("port") == "":
		fle.write(i["tag"][0]+"."+i["tag"][1]+"   "+i["usernam"]+"@"+i["domain"])
        else:
                fle.write(i["tag"][0]+"."+i["tag"][1]+"   "+i["usernam"]+"@"+i["domain"]+":"+i["port"])
        fle.write('\n')
fle.close()                

        
        #dict = ast.literal_eval(reald)
        #print dict       
	#data = json.load(dataf)
#print data
