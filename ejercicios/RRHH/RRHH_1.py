print("EJERCICIO 1: HERENCIA SIMPLE")

class Persona:
    """Clase base - Persona"""
    def init(self, nombre, apellido, cedula, telefono):
        self.nombre   = nombre
        self.apellido = apellido
        self.cedula   = cedula
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Cédula: {self.cedula}")
        print(f"Teléfono: {self.telefono}")

class Empleado(Persona):  #HERENCIA SIMPLE
    """Clase hija que hereda de Persona"""
    def init(self, nombre, apellido, cedula, telefono, codigo_empleado, salario):
        # Llamar al constructor del padre
        super().init(nombre, apellido, cedula, telefono)
        # Atributos propios del empleado
        self.codigo_empleado = codigo_empleado
        self.salario = salario

    def mostrar_info(self):  # Sobrescribir método del padre
        super().mostrar_info()  # Llamar método del padre
        print(f"Código Empleado: {self.codigo_empleado}")
        print(f"Salario: ${self.salario:,}")

        # Probar herencia simple
print("Creando una Persona:")
persona1 = Persona("Ana", "López", "12345678", "300-123-4567")
persona1.mostrar_info()

print("\nCreando un Empleado (hereda de Persona):")
empleado1 = Empleado("Carlos", "García", "87654321", "300-987-6543", "EMP001", 2500000)
empleado1.mostrar_info()

print("\n🔥 EJERCICIO 2: HERENCIA MÚLTIPLE")
print("ContratoDefinido hereda de: Contrato + TipoContrato")

class Contrato:
    """Primera clase padre"""
    def init(self, id_contrato, fecha_inicio, salario_contrato):
        self.id_contrato = id_contrato
        self.fecha_inicio = fecha_inicio
        self.salario_contrato = salario_contrato

    def mostrar_contrato(self):
        print(f"ID Contrato: {self.id_contrato}")
        print(f"Fecha Inicio: {self.fecha_inicio}")
        print(f"Salario: ${self.salario_contrato:,}")

class TipoContrato:
    """Segunda clase padre"""
    def init(self, nombre_tipo, descripcion, beneficios):
        self.nombre_tipo = nombre_tipo
        self.descripcion = descripcion
        self.beneficios = beneficios

    def mostrar_tipo(self):
        print(f"Tipo: {self.nombre_tipo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Beneficios: {'Sí' if self.beneficios else 'No'}")

class ContratoDefinido(Contrato, TipoContrato):  # ← HERENCIA MÚLTIPLE
    """Clase que hereda de DOS clases padres"""
    def init(self, id_contrato, fecha_inicio, salario_contrato, fecha_fin,
                 nombre_tipo, descripcion, beneficios):

        # Inicializar AMBAS clases padre
        Contrato.init(self, id_contrato, fecha_inicio, salario_contrato)
        TipoContrato.init(self, nombre_tipo, descripcion, beneficios)

        # Atributo propio
        self.fecha_fin = fecha_fin

    def mostrar_info_completa(self):
        print("=== INFORMACIÓN DEL CONTRATO DEFINIDO ===")
        self.mostrar_contrato()    # Método de Contrato
        self.mostrar_tipo()        # Método de TipoContrato
        print(f"Fecha Fin: {self.fecha_fin}")

# Probar herencia múltiple
print("Creando un ContratoDefinido (hereda de Contrato Y TipoContrato):")
contrato1 = ContratoDefinido(
    id_contrato=1001,
    fecha_inicio="2024-01-01",
    salario_contrato=3000000,
    fecha_fin="2024-12-31",
    nombre_tipo="Término Fijo",
    descripcion="Contrato de un año",
    beneficios=True
)

contrato1.mostrar_info_completa()