
class Descuentos:
    def __init__(self,id, categoria, nombre,descripcion,tipo,descuento):
        self.id=id
        self.categoria=categoria
        self.nombre=nombre
        self.descripcion=descripcion
        self.tipo=tipo
        self.valor_descuento=descuento

        def calcular_monto(self, sueldo_bruto):
            if self.tipo=="porcentual":
                return sueldo_bruto*self.valor_descuento
            elif self.tipo=="monto_fijo":
                return self.valor_descuento
            return 0






