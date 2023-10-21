from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def email(self):
        return self.__email

    @property
    def contrasenia(self):
        return self.__contrasenia

    def infoUsuario(self):
        pass

    def validar_credenciales(self, email, contrasenia):
        return self.email == email and self.contrasenia == contrasenia