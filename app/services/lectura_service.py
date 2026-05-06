from datetime import datetime # Importante añadir esta importación

class LecturaService:
    def __init__(self, repo):
        self.repo = repo

    def crear(self, db, data):
        data_dict = data.dict()

        # 1. Asignar la fecha actual (esto resuelve el Error 500)
        if "fecha" not in data_dict or data_dict["fecha"] is None:
            data_dict["fecha"] = datetime.now()

        # 2. Calcular el consumo automáticamente
        if data_dict.get("lectura_anterior") is not None:
            data_dict["consumo"] = (
                data_dict["lectura_actual"] - data_dict["lectura_anterior"]
            )
        else:
            data_dict["consumo"] = 0 # Valor por defecto si es la primera lectura

        return self.repo.create(db, data_dict)