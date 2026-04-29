from sqlalchemy.orm import Session
from app.models.Lectura import Lectura
from app.models.Factura import Factura
from app.models.DetalleFactura import DetalleFactura
from app.models.Medidor import Medidor
from app.models.Tarifa import Tarifa
from datetime import datetime

class CobroService:
    def generar_factura_mensual(self, db: Session, id_cliente: str):
        # 1. Buscar todas las lecturas del cliente que NO estén sincronizadas (no facturadas)
        lecturas_pendientes = db.query(Lectura).join(Medidor).filter(
            Medidor.id_cliente == id_cliente,
            Lectura.sincronizado == False
        ).all()

        if not lecturas_pendientes:
            return None

        # 2. Calcular total (obteniendo precio de la tarifa del medidor)
        total_monto = 0
        detalles_a_crear = []

        for lectura in lecturas_pendientes:
            # Buscamos la tarifa asociada al medidor de esta lectura
            medidor = db.query(Medidor).filter(Medidor.id_medidor == lectura.id_medidor).first()
            tarifa = db.query(Tarifa).filter(Tarifa.id_tarifa == medidor.id_tarifa).first()
            
            precio = tarifa.precio_por_m3 if tarifa else 1.0 # default si no hay tarifa
            monto_lectura = float(lectura.consumo) * float(precio)
            total_monto += monto_lectura
            
            detalles_a_crear.append({
                "id_lectura": lectura.id_lectura,
                "monto": monto_lectura
            })

        # 3. Crear la Factura (Cabecera)
        nueva_factura = Factura(
            id_cliente=id_cliente,
            total=total_monto,
            saldo=total_monto,
            estado="pendiente",
            periodo=datetime.now().strftime("%Y-%m"),
            fecha_emision=datetime.now()
        )
        db.add(nueva_factura)
        db.flush() # Para obtener el id_factura generado

        # 4. Crear Detalles y marcar lecturas como sincronizadas
        for item in detalles_a_crear:
            nuevo_detalle = DetalleFactura(
                id_factura=nueva_factura.id_factura,
                id_lectura=item["id_lectura"],
                monto=item["monto"]
            )
            db.add(nuevo_detalle)
            
            # Actualizar lectura para que no se vuelva a facturar
            lectura_db = db.query(Lectura).filter(Lectura.id_lectura == item["id_lectura"]).first()
            lectura_db.sincronizado = True

        db.commit()
        db.refresh(nueva_factura)
        return nueva_factura

cobro_service = CobroService()