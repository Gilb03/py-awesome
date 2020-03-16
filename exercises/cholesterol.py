LDL= 50
HDL = 70
TRI = 130

Total = LDL + HDL + (TRI/5.0)

if (LDL < 100) and (HDL > 60) and (TRI < 150) and (Total < 200):
    print("Cholesterol looks great!")
elif (LDL > 130) or (HDL > 50) or (TRI > 200) or (Total > 240):
    print("Cholesterol looks fucked up")
else:
    print("You almost fucked upo out here , fammo.") 