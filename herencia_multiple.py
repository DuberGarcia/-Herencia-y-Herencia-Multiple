# Herencia Multiple

# class Asociado:
#     def activar_asociado(self):
#         print("Asociado activado")

# class Empleado:
#     def activar_empleado(self):
#         print("Empleado activado")


# class Dependiente(Asociado, Empleado):
#     pass


# duber = Dependiente()
# duber.activar_asociado()
# duber.activar_empleado()

# # [<class '__main__.Dependiente'>, 
# # <class '__main__.Asociado'>, <class '__main__.Empleado'>, <class 'object'>]

# print(Dependiente.mro())

class A:
    def metodo_a(self):
        print("Metodo A")
 
class B(A):
    def metodo_b(self):
        print("Metodo B")
 
class C(A):
    def metodo_c(self):
        print("Metodo C")
 
class D(B, C):
    def metodo_d(self):
        print("Metodo D")  
 
d = D()
d.metodo_a()
d.metodo_b()
d.metodo_c()
d.metodo_d()

d.m

print(D.mro())

