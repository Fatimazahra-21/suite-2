n = int(input("entrer n :"))
while n < 2:
n = int(input("entrer n :"))
Ui = 0
Uj = 1
print("les termes de la suite sont :")
print(Ui)
print(Uj)
for i in range(n-1):
U = Ui + Uj
print(Uj)
Ui = Uj
Uj = U
