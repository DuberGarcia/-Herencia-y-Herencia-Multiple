# Sesión 2: Herencia

# Herencia permite heredar atríbutos y métodos de una clase padre a una clase hija
# Ayuda con la rehusabilidad y extensibilidad del código

class Asociado:
    def __init__(self, nombre: str, es_activo: bool):
        self.nombre = nombre
        self.es_activo = es_activo

    def crear_cuenta(self):
        print(f"Cuenta a nombre de {self.nombre} creada.")

    def imprimir_asociado(self):
        print(f"Asociado {self.nombre} creado")


class Dependiente(Asociado):
    pass

class Independiente(Asociado):
    pass


juan = Independiente("Juan", True)
karolina = Dependiente("Carolina", False)

print(juan.nombre)
juan.imprimir_asociado()
karolina.imprimir_asociado()

