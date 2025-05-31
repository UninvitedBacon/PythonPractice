

import random
randomoptions = ["true","false"]
valid="false"
while (valid=="false"):
    option1 = input ("the cat is about to puch the vase off of the table. What will you do? \n(1) kill the cat. \n(2) stop the cat \n(3) catch the vace \n(4) do nothing\n")
    if option1=="1":
        option2_1 = print ("You sucsessfully shoot the cat before it gets to the vase")
        catliving = "false"
        vaseintack = "true"
        valid = "true"
    elif option1=="2":
        option2_2 = print ("The cat scratches you, but you stop it from breaking the vase")
        catliving = "true"
        vaseintack = "true"
        valid = "true"
    elif option1=="3":
        option1_3_sucsess = random.choice (randomoptions)
        if (option1_3_sucsess == "true"):
            option2_3a = print ("you catch it in time, and the vase is fine")
            catliving = "true"
            vaseintack = "true"
            valid = "true"
        if (option1_3_sucsess=="false"):
            option2_3b = print ("you do not catch the vase in time, and it shatters")
            catliving = "true"
            vaseintack = "flase"
            valid = "true"
    elif option1=="4":
        option2_4 = print ("... The vase shatters")
        catliving = "true"
        vaseintack = "flase"
        valid = "true"
    else:
        print ("just type a number",option1,"is invalid")

valid="false"

while (valid=="false"):
    if (catliving=="true") and (vaseintack=="true"):
        input ("")
    if (catliving=="false") and (vaseintack=="true"):
        input ("You realize that the cat's owner is coming soon. What will you do? \n(1) prepare for combat \n(2) appoligize \n(3) hide the cat \n(4) tell the owner the cat deserves it\n")
    if (catliving=="true") and (vaseintack=="false"):
        input ("")
