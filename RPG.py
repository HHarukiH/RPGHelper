#Após salvar
#executar Git Pasta
#git add .
#git commit -m "modificação feita" // o que alterou
#git push origin main
sArm=[600, 20, 15, 250, 0, 0, 17, 0, 43, 2]
sIsa=[500, 10, 6]
sCar=[200, 50, 15, 200]
sFri=[]
sHen=[]
sGF=[100, 10,]
sGA=[50, 7, 15]
sHF=[]
sHA=[]
sHM=[]
sMB=[]
btl=[]
while True:
    psr=input("personagem, btl:")
    if psr=="btl":
        psr=input("def, print")
        if psr=="def":
            psr=input("quem:")
            aco=int(input("quantos"))
            btl=[psr]*int(aco)
        elif psr=="print":
            print(btl)
    elif psr=="arm" or psr=="Arm":
        aco=input("atk, dan, buf, sts, esc:")
        if aco=="atk":
            aci=input("atk:")
            mir=input("em quem?[0-n]:")
            btl
        elif aco=="dan":
            aci=input("dan:")
            sArm[0]-=int(aci)-sArm[1]
            print (sArm)
        elif aco=="buf":
            aci=input("buf:")
        elif aco=="sts":
            print (sArm)