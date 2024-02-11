a:int=0
filename="my.html"
print("\x1bc\x1b[41;30m")
f1=open(filename,"r")
files=f1.read()
f1.close()
splits=files.split(">")
counter=0
for n in splits:
    n=n.replace("\n","")
    n=n.replace("\r","")
    tags=n.split("<")

    counter=0
    if len(tags)==2 and len(tags[0])>0:
        print("\t",end="")
    for ta in tags:
        ta=ta.strip()
        if counter==0:
            if len(ta)>0:
               print(ta)
        else:
            varsn=ta.split(" ")
            for varn in varsn:
                varn=varn.strip()
                if len(varn)>0:
                    print(varn)
        
        counter+=1
        
    