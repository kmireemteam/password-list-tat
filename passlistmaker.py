import os
os.system("")
class COLOR():
    RED="\033[31m"
    GREEN="\033[32m"
    YELLOW="\033[33m"
inputs=input(COLOR.RED+"Your inputs(split them by ';'):"+COLOR.YELLOW)
word=inputs.split(";")
out_num=0
for num in range(len(word)):
    out_num+=len(word)**(num+1)
build="import sys\n"
build+="words="+str(word)+"\n"
build+="file=open('passwords.txt','w')\n"
build+="_out_num="+str(out_num)+"\n"
build+="prog_num=1\n"
for i in range(len(word)):
    tab=""
    output=""
    for j in range(i+1):
        build+=tab+"for a"+str(j)+" in words:\n"
        tab+="   "
    for k in range(i+1):
        output+="a"+str(k)+"+"
    build+=tab+"file.write("+output[:len(output)-1]+"+chr(10))\n"
    build+=tab+"progress=str(prog_num)+' of '+str(_out_num)\n"
    build+=tab+"prog_num+=1\n"
    build+=tab+"sys.stdout.write(progress)\n"
    build+=tab+"sys.stdout.flush()\n"
    build+=tab+"sys.stdout.write(chr(8)*len(progress))\n"
build+="file.close()"
exec(build)
print(COLOR.GREEN+str(out_num)+" passwords saved in passwords.txt"+"\033[39m")
