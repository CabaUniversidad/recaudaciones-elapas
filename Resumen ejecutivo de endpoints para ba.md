# Resumen ejecutivo de endpoints para backend MVP

## Objetivo

Definir los endpoints mínimos que necesita el backend para soportar el flujo principal del MVP del sistema **ELAPAS - Recaudaciones y Cortes**.

## Flujo principal a cubrir

1. El brigadista inicia sesión.
2. Busca un cliente.
3. Obtiene el medidor asociado.
4. Registra una lectura o un corte desde la app móvil.
5. La web consulta lecturas, cortes, deuda y resumen general.

---

# Endpoints mínimos prioritarios

## 1. Autenticación

### POST `/auth/login`
Permite iniciar sesión desde móvil y web.

### GET `/auth/me`
Devuelve la información del usuario autenticado.

---

## 2. Clientes

### GET `/usuarios/buscar?q=`
Buscar cliente por nombre, apellido, CI u otro criterio.

### GET `/usuarios/{id_usuario}`
Ver detalle básico del cliente.

### GET `/usuarios`
Listar clientes para la web.

---

## 3. Medidores

### GET `/medidores/usuario/{id_usuario}`
Obtener el medidor asociado a un cliente.

### GET `/medidores/buscar?q=`
Buscar medidor por código o por relación con usuario.

### GET `/medidores/{id_medidor}`
Detalle de medidor.

---

## 4. Lecturas

### POST `/lecturas`
Registrar lectura desde móvil.

### GET `/lecturas`
Listar lecturas para la web.

### GET `/lecturas/{id_lectura}`
Ver detalle de lectura.

### GET `/lecturas/medidor/{id_medidor}`
Historial por medidor.

---

## 5. Cortes

### POST `/cortes`
Registrar corte desde móvil.

### GET `/cortes`
Listar cortes para la web.

### GET `/cortes/{id_corte}`
Ver detalle de corte.

### GET `/cortes/medidor/{id_medidor}`
Historial de cortes por medidor.

---

## 6. Deuda y facturas

### GET `/usuarios/{id_usuario}/deuda`
Consultar deuda pendiente del cliente.

### GET `/facturas/usuario/{id_usuario}`
Consultar facturas del cliente.

### GET `/usuarios/{id_usuario}/estado-cuenta`
Resumen de deuda, facturas y pagos.

---

## 7. Dashboard

### GET `/dashboard/resumen`
Resumen general para la pantalla principal web.

Debe devolver algo como:
- total de usuarios
- total de medidores
- lecturas del día
- cortes del día
- facturas pendientes
- monto total pendiente

---

# Prioridad real de implementación

## Prioridad alta
Estos son los más importantes para que el MVP funcione:

- `POST /auth/login`
- `GET /usuarios/buscar?q=`
- `GET /medidores/usuario/{id_usuario}`
- `POST /lecturas`
- `POST /cortes`
- `GET /lecturas`
- `GET /cortes`
- `GET /usuarios/{id_usuario}/deuda`
- `GET /dashboard/resumen`

## Prioridad media
Se pueden hacer después si el tiempo alcanza:

- `GET /usuarios`
- `GET /usuarios/{id_usuario}`
- `GET /medidores/buscar?q=`
- `GET /medidores/{id_medidor}`
- `GET /lecturas/{id_lectura}`
- `GET /lecturas/medidor/{id_medidor}`
- `GET /cortes/{id_corte}`
- `GET /cortes/medidor/{id_medidor}`
- `GET /facturas/usuario/{id_usuario}`
- `GET /usuarios/{id_usuario}/estado-cuenta`

---

# Recomendaciones clave para backend

## 1. El backend debe calcular el consumo
No conviene que el frontend calcule `consumo`.  
Debe salir de:

`lectura_actual - lectura_anterior`

## 2. Conviene devolver datos enriquecidos
Por ejemplo:
- medidor con datos del usuario
- lectura con datos del medidor y cliente
- corte con datos del medidor y cliente

## 3. No hacer CRUD completo de todo
Para el MVP no hace falta desarrollar todo el sistema.  
Lo importante es cubrir:
- login
- búsqueda
- registro de lectura
- registro de corte
- consulta de deuda
- dashboard básico

## 4. Revisar autenticación
La tabla `empleado` no muestra aún campos claros para login como:
- usuario o correo
- password hash

Eso debe definirse en backend antes de cerrar autenticación.

---

# Lista ultra resumida

```text
POST /auth/login
GET  /auth/me

GET  /usuarios
GET  /usuarios/{id_usuario}
GET  /usuarios/buscar?q=

GET  /medidores/{id_medidor}
GET  /medidores/usuario/{id_usuario}
GET  /medidores/buscar?q=

POST /lecturas
GET  /lecturas
GET  /lecturas/{id_lectura}
GET  /lecturas/medidor/{id_medidor}

POST /cortes
GET  /cortes
GET  /cortes/{id_corte}
GET  /cortes/medidor/{id_medidor}

GET  /facturas/usuario/{id_usuario}
GET  /usuarios/{id_usuario}/deuda
GET  /usuarios/{id_usuario}/estado-cuenta

GET  /dashboard/resumen
```

# Conclusión

Si backend implementa primero los endpoints de prioridad alta, el equipo ya podrá avanzar con la app móvil y la interfaz web sin depender de todo el sistema completo.