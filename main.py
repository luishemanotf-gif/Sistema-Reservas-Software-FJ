from cliente import Cliente
from servicios_especializados import ReservaSala, AlquilerEquipos, AsesoriaEspecializada
from reserva import Reserva
from logger import registrar_error

def ejecutar_sistema():

    print("===== SISTEMA DE RESERVAS SOFTWARE FJ =====")

    try:

        # Crear clientes
        cliente1 = Cliente("Juan Perez", "juan@email.com")
        cliente2 = Cliente("Maria Lopez", "maria@email.com")

        print("Clientes creados correctamente")

        # Crear servicios
        sala = ReservaSala("Sala de reuniones", 50)
        equipo = AlquilerEquipos("Alquiler de proyector", 30)
        asesoria = AsesoriaEspecializada("Asesoria en software", 80)

        print("Servicios creados correctamente")

        # Reserva válida
        reserva1 = Reserva(cliente1, sala, 3)
        costo1 = reserva1.procesar()
        reserva1.confirmar()

        print("Reserva confirmada - Costo:", costo1)

        # Otra reserva válida
        reserva2 = Reserva(cliente2, equipo, 2)
        costo2 = reserva2.procesar()
        reserva2.confirmar()

        print("Reserva confirmada - Costo:", costo2)

    except Exception as e:
        registrar_error(e)
        print("Error en el sistema:", e)

    # Ejemplos con errores controlados
    operaciones = [
        ("Cliente inválido", "", "correo"),
        ("Email inválido", "Pedro", "pedrocorreo"),
    ]

    for nombre, email in operaciones:

        try:
            cliente_error = Cliente(nombre, email)
            print("Cliente creado:", cliente_error.obtener_nombre())

        except Exception as e:
            registrar_error(e)
            print("Error detectado:", e)

    # Reservas adicionales para completar operaciones
    try:

        cliente3 = Cliente("Carlos", "carlos@email.com")
        reserva3 = Reserva(cliente3, asesoria, 4)

        costo3 = reserva3.procesar()

        print("Costo asesoría:", costo3)

    except Exception as e:
        registrar_error(e)

    try:

        reserva4 = Reserva(cliente1, sala, -2)
        costo4 = reserva4.procesar()

        print("Costo:", costo4)

    except Exception as e:
        registrar_error(e)
        print("Error en reserva:", e)

    print("===== SISTEMA FINALIZADO =====")


if __name__ == "__main__":
    ejecutar_sistema()
