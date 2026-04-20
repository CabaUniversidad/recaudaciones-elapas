# recaudaciones-elapas

Sistema de gestión de recaudaciones para ELAPAS con arquitectura modular. Incluye API REST en FastAPI, aplicación móvil con soporte offline y portal web con dashboard e indicadores KPI.

---

## 1. Descripción general

El sistema permite gestionar:

* Registro de usuarios y medidores
* Lectura de consumo en campo
* Cálculo de deuda
* Generación de facturas
* Consulta de estado de cuenta
* Pagos mediante QR
* Monitoreo mediante dashboard

Diseñado para operar con conectividad limitada y múltiples tipos de usuario.

---

## 2. Arquitectura del sistema

El proyecto está dividido en tres componentes principales:

* **Backend (API REST)** → lógica de negocio y datos
* **Frontend Web** → portal de usuario y administración
* **Aplicación Móvil** → uso en campo con soporte offline

---

## 3. Tecnologías utilizadas

* Backend: FastAPI
* Base de datos: PostgreSQL / SQL Server
* Web: React
* Mobile: Flutter o React Native
* Control de versiones: Git

---

## 4. Configuración del entorno

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Web

```bash
cd web
npm install
npm start
```

### Mobile

```bash
cd mobile
flutter pub get
flutter run
```

---

## 5. Workflow de desarrollo (Feature-Based)

Se trabaja con ramas por funcionalidad para mantener orden y control.

### Ramas principales

* `main` → versión estable
* `develop` → integración
* `feature/*` → desarrollo individual

---

### Crear una feature

```bash
git checkout develop
git pull
git checkout -b feature/nombre-feature
```

Ejemplos:

```bash
feature/api-lecturas
feature/mobile-offline
feature/web-dashboard
```

---

### Integrar una feature

```bash
git push origin feature/nombre-feature

git checkout develop
git merge feature/nombre-feature
git push
```

Eliminar rama:

```bash
git branch -d feature/nombre-feature
```

---

### Paso a versión estable

```bash
git checkout main
git merge develop
git push
```

---

## 6. Convención de commits

Formato:

```bash
tipo:nombre/mensaje
```

Ejemplo:

```bash
git commit -m "feat:dev1/registro de lectura de medidor"
```

---

### Tipos de commit

| Tipo     | Uso                                       | Ejemplo de mensaje                          | Comando ejemplo                                         |
| -------- | ----------------------------------------- | ------------------------------------------- | ------------------------------------------------------- |
| feat     | Nueva funcionalidad                       | feat:dev1/registro de lectura               | git commit -m "feat:dev1/registro de lectura"           |
| fix      | Corrección de errores                     | fix:dev2/error en cálculo de deuda          | git commit -m "fix:dev2/error en cálculo de deuda"      |
| refactor | Mejora interna sin cambiar comportamiento | refactor:dev1/separar lógica de facturación | git commit -m "refactor:dev1/separar lógica"            |
| docs     | Cambios en documentación                  | docs:team/actualizar README                 | git commit -m "docs:team/actualizar README"             |
| chore    | Tareas técnicas, configuración            | chore:devops/configurar base de datos       | git commit -m "chore:devops/configurar base de datos"   |
| test     | Agregar o modificar pruebas               | test:qa/pruebas de cálculo                  | git commit -m "test:qa/pruebas de cálculo"              |
| style    | Cambios de formato (sin lógica)           | style:webdev/formatear componentes          | git commit -m "style:webdev/formatear componentes"      |
| perf     | Mejora de rendimiento                     | perf:dev1/optimizar consultas               | git commit -m "perf:dev1/optimizar consultas"           |
| build    | Cambios en dependencias o build           | build:devops/actualizar librerías           | git commit -m "build:devops/actualizar librerías"       |
| ci       | Integración continua                      | ci:devops/agregar pipeline                  | git commit -m "ci:devops/agregar pipeline"              |
| revert   | Revertir cambios                          | revert:dev1/revertir cálculo incorrecto     | git commit -m "revert:dev1/revertir cálculo incorrecto" |

---

## 7. Reglas de trabajo

* No trabajar en `main` directamente
* No trabajar en `develop` directamente
* Una feature = una responsabilidad
* Commits pequeños y claros
* Ramas temporales

---

## 8. Ejemplos de features

* feature/api-lecturas
* feature/api-deuda
* feature/mobile-registro
* feature/mobile-offline
* feature/web-consulta
* feature/dashboard-kpi

---

## 9. Objetivo del proyecto

Mejorar la recaudación mediante:

* Reducción de errores
* Mayor velocidad de atención
* Información en tiempo real
* Soporte a decisiones

---

## 10. Estado del proyecto

En desarrollo (MVP por iteraciones).
