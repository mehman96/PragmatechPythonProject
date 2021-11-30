# Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
a=input("1 ci eded daxil edin :")
b=input("2 ci ededi daxil edin :")
c=int(input(" 3 cü ededi daxil edin :"))
d=int(input(" 4 cü ededi daxil edin :"))

if a==b==c==d:
    print ('Ededler beraberdir')
else:
    print(max(a,b,c,d))