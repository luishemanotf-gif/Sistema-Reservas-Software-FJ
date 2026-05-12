class Cliente:

    def __init__(self, nombre, email):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in email:
            raise ValueError("Email inválido")

        self.__nombre = nombre
        self.__email = email

    def obtener_nombre(self):
        return self.__nombre

    def obtener_email(self):
        return self.__email
