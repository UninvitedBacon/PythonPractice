import os
import time
done="false"
y=[]
valid="false"
menu = "open"
os.system('cls')
while menu=="open":
    print ("you need to make a cheeseburger for some buff dude so he does not kill you")
    while (done=="false"):
    while valid=="false":
        x=input("what will you put on it?\n(1) lettuce\n(2) cheese\n(3) beef \n(4) explosives\n(5) done")
        if (x=="1"):
            x="lettuce"
            valid="true"
        elif (x=="2"):
            x="cheese"
            valid="true"
        elif (x=="3"):
            x="beef"
            valid="true"
        elif (x=="4"):
            x="explosives"
            valid="true"
        else:
            print ("that is invalid")
        areyoudone=input("are you done?\n(1) yes\n(2) no\n")
        valid="false"
        if (areyoudone=="1"):
            done="true"
        y.append(x)
    menu="closed"
print ("your cheseburger has",y)