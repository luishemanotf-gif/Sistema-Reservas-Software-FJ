from cliente import Cliente
from servicios_especializados import ReservaSala
from reserva import Reserva
from logger import registrar_error

try:

    cliente1 = Cliente("Juan", "juan@email.com")
    servicio = ReservaSala("Sala Conferencias", 50)

    reserva = Reserva(cliente1, servicio, 3)

    costo = reserva.procesar()

    print("Costo:", costo)

    reserva.confirmar()

except Exception as e:
    registrar_error(e)
