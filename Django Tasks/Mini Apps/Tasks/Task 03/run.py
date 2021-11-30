# Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil 
# etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın).
#  Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

fruit={
    "ananas":"30$",
    "alma" :"50$",
    "armud" :"70$",
    "uzum" : "434$"
}
a=fruit

print(fruit)

a=input()
if a in fruit:
    print("var\n"+"Qiymet:"+fruit[a])
else:
    print('yoxdu')