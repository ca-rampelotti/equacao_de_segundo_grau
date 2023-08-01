import math
a = float(input("Entre com o coeficiente do termo quadrado: "))
b = float(input("Entre com o coeficiente do termo no primeiro grau: "))
c = float(input("Entre com o coeficiente do termo independente: "))
delta_2 = ((b*b)-(4*a*c))
print (delta_2)
if delta_2 < 0:
    print ("Raízes são números complexos")
else:
    delta = math.sqrt(delta_2)
    print (delta)
    r1 = ((-b) + (delta))/(2*a)
    r2 = ((-b) - (delta))/(2*a)
    print (r1, r2)

def eq_2_grau (a, b, c):
    delta_2 = ((b*b)-(4*a*c))
    print (delta_2)
    if delta_2 < 0:
        return ("Raízes são números complexos")
    elif delta_2 == 0:
        r = (-b)/(2*a)
        return r
    else:
        delta = math.sqrt(delta_2)
        r1 = ((-b) + (delta))/(2*a)
        r2 = ((-b) - (delta))/(2*a)
        return r1,r2
    
a = float(input("Entre com o coeficiente do termo quadrado: "))
b = float(input("Entre com o coeficiente do termo no primeiro grau: "))
c = float(input("Entre com o coeficiente do termo independente: "))
r = eq_2_grau(a, b, c)
print (r)