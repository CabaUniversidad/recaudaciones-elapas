class CobroService:

    def __init__(self, factura_repo, detalle_repo):
        self.factura_repo = factura_repo
        self.detalle_repo = detalle_repo

    def generar_factura(self, db, id_usuario, lecturas):
        total = 0

        factura = self.factura_repo.create(db, {
            "id_usuario": id_usuario,
            "total": 0,
            "estado": "pendiente"
        })

        for lectura in lecturas:
            monto = lectura.consumo * 2  # ejemplo tarifa

            total += monto

            self.detalle_repo.create(db, {
                "id_factura": factura.id_factura,
                "id_lectura": lectura.id_lectura,
                "monto": monto
            })

        factura.total = total
        db.commit()
        db.refresh(factura)

        return factura