print ("\33[34 kimeerteam password list")
n=input("\33[31m your inputs:")
word=n.split(";")
np=0
for i in range(1,len(word)+1):
    np+=len(word)**i
build="import sys\n"
build+="np="+str(np)+"\n"+"i=0\n"
build+='word='+str(word)+"\n"
build+="nl=chr(10)"+"\n"
build+='file=open("kimeer.txt","w")'+"\n"
if len(word)>3:
    wrd=3
else:
    wrd=len(word)
for i in range(wrd):
    H=""
    for j in range(i+1):
        build+=("    "*j)+"for a"+str(j)+" in word:"+"\n"
        H+="a"+str(j)+"+"
    build+=("    "*(i+1))+"file.write("+H[:len(H)-1]+"+nl)"+"\n"
    build+=("    "*(i+1))+"i+=1\n"
    build+=("    "*(i+1))+"b=str(i)+' of '+str(np)\n"
    build+=("    "*(i+1))+"sys.stdout.write(len(b)*'\b')\n"
    build+=("    "*(i+1))+"sys.stdout.flush()\n"
    build+=("    "*(i+1))+"sys.stdout.write(b)\n"
build+="file.close()"
exec(build)
print(str(np)+" passwords saved in kimeer.txt")
