from Funciones_DB import *
from Funciones.Interfaces_Admin import *
from FuncionesLibro.Funciones_Libro import *

class PedidoLibro(Atributos):
    def __init__(self):
        super().__init__()
        self.cond = 0

    db_nombre = "StockLibros.db"
    db_nombredata = "ListaClientes.db"
    
    def consultar(self, query, parameters=()):
        with sql.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def consultarData(self, query, parameters = ()):
        with sql.connect(self.db_nombredata) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def Llamada(self):
        VentanaPrincipal.ventanaPrincipal(self)
        
if __name__ == "__main__":
    app2 = PedidoLibro()
    app2.Llamada()