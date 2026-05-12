from servicio import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de salas para reuniones"


class AlquilerEquipos(Servicio):

    def calcular_costo(self, horas):
        return (self.precio_base * horas) + 10

    def descripcion(self):
        return "Alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):
        return (self.precio_base * horas) * 1.2

    def descripcion(self):
        return "Servicio de asesoría profesional"
