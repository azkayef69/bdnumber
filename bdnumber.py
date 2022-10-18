import random
codes=["017","019","013","014","015","016","018"]

pl=int(input("Pass length(6-11): "))
for i in range(10000):
    x=""
    while len(x)!=8:
      x=str(random.randint(00000000,99999999))
      

    num=str(random.choice(codes))+x
    pw=num[-pl:]
    print (num,pw)