from abc import ABC, abstractmethod

class Atributos():
    def __init__(self):
        self._nombres = None
        self._apellido = None
        self._dni = None
        self._membresia = None
        
class AddProduct(ABC):
    @abstractmethod
    def agregarCliente(self):
        pass

class RemoveProduct(ABC):
    @abstractmethod
    def eliminarCliente(self):
        pass

class ModifyProduct(ABC):
    @abstractmethod
    def modificarCliente(self):
        pass

class ShowStock(ABC):
    @abstractmethod
    def mostrarCliente(self):
        pass

class BackToMenu(ABC):
    @abstractmethod
    def volverMenu(self):
        pass

class Menu(ABC):
    @abstractmethod
    def ventanaPrincipal(self):
        pass