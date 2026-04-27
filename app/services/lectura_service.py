class LecturaService:

    def __init__(self, repo):
        self.repo = repo

    def crear(self, db, data):
        data_dict = data.dict()

        if data_dict.get("lectura_anterior") is not None:
            data_dict["consumo"] = (
                data_dict["lectura_actual"] - data_dict["lectura_anterior"]
            )

        return self.repo.create(db, data_dict)