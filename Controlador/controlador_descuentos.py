import json
from Modelo import descuentos
class controlador_descuentos:
    @staticmethod
    def obtener_descuento_por_id(id_buscado):
        try:
            #abrir el json
            with open("catalogo_descuentos.json","r", encoding="utf-8") as archivo:
                data=json.load(archivo)

            #leer la data
            for d in data["descuentos"]:
                if d("id")==int(id_buscado):
                    #traer la data
                    return descuentos(
                        id=["id"],
                        categoria=["categoria"],
                        nombre=["nombre"],
                        descripcion=["descripcion"],
                        tipo=["tipo"],
                        descuento=["descuento"]
                    )
            return None

        except FileNotFoundError:
            print("[Error de Sistema] el archivo descuentos.json no existe")
            return None
