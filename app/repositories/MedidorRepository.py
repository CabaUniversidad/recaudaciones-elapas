from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.Medidor import Medidor
from app.repositories.BaseRepository import BaseRepository
from app.models.Lectura import Lectura
from app.models.Cliente import Cliente  # <--- ESTO ES LO QUE FALTABA
from app.models.Factura import Factura
class MedidorRepository(BaseRepository[Medidor]):
    def __init__(self):
        super().__init__(Medidor, "id_medidor")

    def create(self, db: Session, data: dict) -> Medidor:
        obj = Medidor(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_by_user(self, db: Session, id_cliente: str):
        return db.query(Medidor).filter(Medidor.id_cliente == id_cliente).all()

    def search_by_user(self, db: Session, q: str):
        return db.query(Medidor).join(Medidor.cliente).filter(
            or_(
                Medidor.cliente.has(ci=q),
                Medidor.cliente.has(nombre=q),
                Medidor.cliente.has(apellido=q)
            )
        ).all()
    def consultar_deuda_publica(self, db: Session, ci: str, codigo_medidor: str):
        # 1. Verificar que el medidor existe y pertenece al cliente con ese CI
        # En el SQL la columna es 'codigo', pero el JSON envía 'codigo_medidor'
        medidor = db.query(Medidor).join(Cliente).filter(
            Cliente.ci == ci,
            Medidor.codigo == codigo_medidor
        ).first()

        if not medidor:
            return None

        # 2. Buscar facturas pendientes asociadas al cliente del medidor
        # El SQL vincula la factura directamente con el id_cliente
        facturas_pendientes = db.query(Factura).filter(
            Factura.id_cliente == medidor.id_cliente,
            Factura.estado == "pendiente"
        ).all()

        total_deuda = sum(f.total for f in facturas_pendientes)

        # 3. Mapeo de resultados
        return {
            "nombre_cliente": medidor.cliente.nombre,
            "apellido_cliente": medidor.cliente.apellido,
            "codigo_medidor": medidor.codigo,
            "total_deuda": float(total_deuda),
            "cantidad_facturas_pendientes": len(facturas_pendientes),
            "facturas": [
                {
                    "periodo": f.periodo,
                    "monto": float(f.total),
                    "fecha_vencimiento": f.fecha_fin.strftime("%Y-%m-%d") if f.fecha_fin else "N/A",
                    "estado": f.estado
                } for f in facturas_pendientes
            ]
        }
medidor_repo = MedidorRepository()