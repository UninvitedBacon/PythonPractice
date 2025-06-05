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
            x=input("what will you put on it?\n(1) lettuce\n(2) cheese\n(3) beef \n(4) explosives\n(5) done\n")
            if (x=="1"):
                z="lettuce"
                y.append(z)
            elif (x=="2"):
                z="cheese"
                y.append(z)
            elif (x=="3"):
                z="beef"
                y.append(z)
            elif (x=="4"):
                z="explosives"
                y.append(z)
            elif (x=="5"):
                valid="true"
                done="true"
            else:
                print (x,"is invalid")
    print ("your cheseburger has",y)
    x=input("is this what you want?\n(1) yes, I am done\n(2) no, I want to restart\n(3) no, I want to continue adding things\n")
    if x=="1":
        print ("Ok, powering off")
        menu="closed"
    elif x=="2":
        print ("ok, try again")
        done="false"
        valid="false"
        y=[]
    elif x=="3":
        done="false"
        valid="false"
        print ("alright you can continue")
1692-370 broth
g letuse
