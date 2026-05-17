# Lab 06 - Búsqueda Inteligente y Redes Bayesianas

## 📋 Descripción General

Este proyecto implementa algoritmos de búsqueda inteligente y sistemas de inferencia bayesiana. Incluye:

- **Búsqueda A* en grafos**: Algoritmo de búsqueda heurística para encontrar rutas óptimas
- **Redes Bayesianas**: Modelo probabilístico para inferencia causal (ej: diagnóstico de enfermedades)
- **API REST**: Servidor FastAPI para acceder a los servicios de búsqueda
- **Visualización**: Herramientas para visualizar grafos y resultados

## 🎯 Objetivos del Laboratorio

Este proyecto es un laboratorio universitario (Inteligencia Artificial - SI) que cubre:

1. Algoritmos de búsqueda heurística (A*)
2. Grafos ponderados y análisis de rutas
3. Modelos probabilísticos (Redes Bayesianas)
4. Inferencia bayesiana para sistemas de decisión
5. Desarrollo de APIs REST para IA

---

## 📁 Estructura del Proyecto

```
lab6_intelligent_search/
├── src/lab6_intelligent_search/
│   ├── api/
│   │   └── main.py                 # Servidor FastAPI
│   ├── bayesian/
│   │   └── disease_network.py      # Red Bayesiana para diagnóstico de enfermedades
│   ├── graph/
│   │   ├── graph_builder.py        # Construcción de grafos
│   │   ├── heuristic.py            # Funciones heurísticas para A*
│   │   └── [otros componentes]
│   ├── models/
│   │   └── route_models.py         # Modelos Pydantic para validación
│   └── services/
│       └── search_service.py       # Servicio de búsqueda A*
├── tests/
│   └── test_astar.py               # Tests unitarios
├── visualize.py                    # Script de visualización de grafos
└── pyproject.toml                  # Configuración del proyecto
```

---

## 🔧 Componentes Principales

### 1. **Búsqueda A* en Grafos** (`graph/`)

**Archivos:**
- `graph_builder.py`: Construye un grafo de ejemplo con 6 nodos (A-F) y aristas ponderadas
- `heuristic.py`: Define valores heurísticos para cada nodo
- `search_service.py`: Implementa el algoritmo A* usando NetworkX

**Grafo de ejemplo:**
```
    A ---1--- B ---2--- D
    |         |
    4         5
    |         |
    C ---3--- E ---1--- F
```

**Características:**
- Encuentra rutas óptimas entre dos nodos
- Retorna el camino completo y su costo total
- Utiliza heurística para optimizar la búsqueda

### 2. **Redes Bayesianas** (`bayesian/`)

**Archivo:** `disease_network.py`

Implementa un modelo probabilístico para diagnóstico de enfermedades con:

- **Nodos**: Enfermedad, Fiebre, Test
- **CPD (Conditional Probability Distributions)**:
  - P(Enfermedad) = [0.1, 0.9] (10% con enfermedad, 90% sin)
  - P(Fiebre|Enfermedad) y P(Test|Enfermedad)
  
- **Inferencia**: Calcula probabilidades condicionales:
  - P(Enfermedad | Fiebre = Sí)
  - P(Enfermedad | Test = Positivo)

**Uso:** Diagnóstico médico probabilístico basado en síntomas y pruebas

### 3. **API REST** (`api/`)

**Archivo:** `main.py`

Servidor FastAPI con endpoint:

```
POST /find-route
Body: {"start": "A", "goal": "F"}
Response: {"path": ["A", "B", "E", "F"], "cost": 9}
```

### 4. **Visualización** (`visualize.py`)

Renderiza el grafo usando Matplotlib:
- Dibuja nodos y aristas
- Etiqueta pesos de aristas
- Facilita análisis visual de la estructura

---

## 📦 Dependencias

```
networkx (>=3.6.1)        # Análisis y manipulación de grafos
matplotlib (>=3.10.9)     # Visualización
fastapi (>=0.136.1)       # Framework web
uvicorn (>=0.47.0)        # Servidor ASGI
pydantic (>=2.13.4)       # Validación de modelos
pgmpy (>=1.1.2)           # Redes Bayesianas
pytest (>=9.0.3)          # Testing
```

---

## 🚀 Instalación

### 1. Requisitos previos
- Python 3.14.4 o superior
- pip o poetry

### 2. Clonar repositorio
```bash
git clone <url-del-repo>
cd Ucv-ate-si-lab-06/lab6_intelligent_search
```

### 3. Instalar dependencias
```bash
# Con poetry
poetry install

# O con pip
pip install -e .
```

---

## 💻 Uso

### Ejecutar el servidor API

```bash
cd lab6_intelligent_search
uvicorn src.lab6_intelligent_search.api.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

**Documentación interactiva:** `http://localhost:8000/docs`

### Hacer una solicitud de búsqueda

```bash
curl -X POST "http://localhost:8000/find-route" \
  -H "Content-Type: application/json" \
  -d '{"start": "A", "goal": "F"}'
```

**Respuesta esperada:**
```json
{
  "path": ["A", "B", "E", "F"],
  "cost": 9
}
```

### Visualizar el grafo

```bash
python visualize.py
```

Se abrirá una ventana con la visualización del grafo.

### Ejecutar inferencia bayesiana

```bash
python -m lab6_intelligent_search.bayesian.disease_network
```

Mostrará probabilidades de enfermedad dado síntomas y pruebas.

---

## 🧪 Testing

Ejecutar pruebas unitarias:

```bash
# Con pytest
pytest tests/

# Con verbose
pytest tests/ -v
```

**Test actual:**
- `test_astar_route()`: Verifica que el camino de A a F sea [A, B, E, F]

---

## 📊 Ejemplo de Uso Completo

### Python (directo)

```python
from lab6_intelligent_search.services.search_service import find_route

# Buscar ruta de A a F
resultado = find_route('A', 'F')

print(f"Camino: {resultado['path']}")
print(f"Costo: {resultado['cost']}")
```

### Inferencia Bayesiana

```python
from pgmpy.inference import VariableElimination
from lab6_intelligent_search.bayesian.disease_network import inference

# P(Enfermedad | Fiebre)
resultado = inference.query(variables=['Disease'], evidence={'Fever': 1})
print(resultado)
```

---

## 🎓 Conceptos Teóricos

### Algoritmo A*

- Combina búsqueda de costo uniforme con heurística
- **f(n) = g(n) + h(n)** donde:
  - g(n) = costo real desde inicio
  - h(n) = heurística hasta objetivo
- Garantiza encontrar la ruta óptima si h(n) es admisible

### Redes Bayesianas

- Grafos acíclicos dirigidos (DAG) con probabilidades condicionales
- Permiten inferencia probabilística eficiente
- Aplicaciones: diagnóstico médico, sistemas expertos, análisis de riesgos

---
