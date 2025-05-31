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
sGA=[]
sHF=[]
sHA=[]
sHM=[]
sMB=[]
while True:
    psr=input("personagem:")
    if psr=="arm" or psr=="Arm":
        aco=input("atk, dan, buf, esc:")
        if aco=="atk":
            aci=input("atk:")
        elif aco=="dan":
            aci=input("dan:")
            sArm[0]-=int(aci)-sts[1]
            print (sts)
        elif aco=="buf":
            aci=input("buf:")