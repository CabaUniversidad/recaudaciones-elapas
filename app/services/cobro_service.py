def calcular_pago(lectura_actual: float, lectura_anterior: float, precio_unitario: float):
    # Sacamos la diferencia de lo que se gastó
    consumo = lectura_actual - lectura_anterior
    # Multiplicamos por el precio
    total = consumo * precio_unitario
    return total, consumo