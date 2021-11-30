# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini vert(in.
# a=int(input("1 ci eded daxil edin :"))
# b=int(input("2 ci ededi daxil edin :"))
# c=int(input(" 3 cü ededi daxil edin :"))
# d=int(input(" 4 cü ededi daxil edin :"))

# if a==b==c==d:
#     print(a*a)
# else:
#     print(a+b+c+d)

my_list=[]
cem=0
for i in range(1,5):
    a=float(input(f"{i}-ci ededi daxil edin : "))
    my_list.append(a)
print(my_list)
if my_list[0]==my_list[1] and my_list[0]==my_list[2] and my_list[0]==my_list[3]:
    s=my_list[0]**2
    print(s)
else:
    for i in my_list:
        cem+=i
    print(cem)

