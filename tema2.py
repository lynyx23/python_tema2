text="Faceti o propozitie de zece cuvinte care sa contina cuvinte"
text=text.replace(" sa contina cuvinte","")

print(text,'\n')

def f(x):
    return lambda a:a%x;

r10=f(10)
r100=f(100)
r1000=f(1000)

y=input("Introduceti numarul : ")
y=int(y)
print("\nRestul impartirii la 10: {:6d}".format(r10(y)))
print("Restul impartirii la 100: {:5d}".format(r100(y)))
print("Restul impartirii la 1000: {:4d}\n".format(r1000(y)))

r2=f(2)

baza2=0
pow=1
while y>0:
    baza2=baza2+r2(y)*pow
    pow=pow*10
    y=int(y/2)
print("Numarul convertit in baza 2:",baza2)
