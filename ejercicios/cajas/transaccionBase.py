class TransaccionBase:

    prefijoComprobante = ''
    sucursalComprobante = ''
    numeroComprobante = ''

    indicadorReversion = ''

    prefijoAnulacion = ''
    sucursalAnulacion = ''
    numeroAnulacion = '' 

    def __init__(self, codigo: int, usuario: str, asociado: int, tercero: str, hora: str, servicio: int, tipoTransaccion: int, valor: int):
        
        self.codigo = codigo
        self.usuario = usuario
        self.asociado = asociado
        self.tercero = tercero
        self.hora = hora
        self.servicio = servicio
        self.tipoTransaccion = tipoTransaccion
        self.valor = valor

    def realizar_transaccion(self):

        print(f"Se ha realizado la transacción {self.tipoTransaccion} al servicio {self.servicio} por valor de ${self.valor}")

    def contabilizar_transaccion(self):

        print(f"Se ha realizado la contabilización de la transacción por ${self.valor} en la cuenta {self.servicio} del asociado {self.tercero}")
        self.prefijoComprobante = 'P'
        self.sucursalComprobante = 'BU'
        self.numeroComprobante = '12345'

    def imprime_comprobante(self):

        self.comprobanteMovimiento = self.prefijoComprobante + self.sucursalComprobante + self.numeroComprobante
        print(f"Se imprime comprobante {self.comprobante}")

    def reversar_transaccion(self):

        self.comprobanteReversion = self.prefijoAnulacion + self.sucursalAnulacion + self.numeroAnulacion
        print(f"Se genera comprobante de reversión {self.comprobanteReversion} para el movimiento {self.comprobanteMovimiento} del tercero {self.tercero}")
        self.indicadorReversion = 'R'


class TransaccionAhorro(TransaccionBase):

    cuenta = None

    def insertar_cuenta(self):
        print(f"Se ha añadido la cuenta correspondiente {self.servicio} en la transacción.")

class TransaccionCredito(TransaccionBase):

    carcod = None
     
    def insert_cartera(self):
        print(f"Se ha añadido el código de cartera {self.carcod} a la transacción.")

class TransaccionCombinada(TransaccionBase, TransaccionAhorro, TransaccionCredito):

    def insertar_registros(self):
        print(f"Se ha ingresado el código de cartera y la cuenta del servicio.")