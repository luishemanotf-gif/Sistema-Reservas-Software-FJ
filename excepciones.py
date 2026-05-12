class ErrorReserva(Exception):
    pass


class ClienteInvalido(ErrorReserva):
    pass


class ServicioNoDisponible(ErrorReserva):
    pass
