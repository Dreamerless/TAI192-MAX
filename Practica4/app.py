from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='API de Tareas',
    description='API para gestionar tareas - Acosta Gonzalez Maximiliano',
    version='1.0.1'
)

# Lista para almacenar tareas (simulando una base de datos)
tareas = [
    {"id": 1, "titulo": "Hacer la compra", "descripcion": "Comprar alimentos para la semana", "vencimiento": "2023-12-01", "estado": "pendiente"},
    {"id": 2, "titulo": "Estudiar FastAPI", "descripcion": "Aprender a usar FastAPI", "vencimiento": "2023-12-05", "estado": "en progreso"},
    {"id": 3, "titulo": "Hacer ejercicio", "descripcion": "Ir al gimnasio", "vencimiento": "2023-12-03", "estado": "pendiente"}
]

# Endpoint home
@app.get('/')
def home():
    return {'hello': 'world FastAPI'}
    
    # Endpoint consultar todas las tareas
@app.get('/todosTareas', tags=['operaciones CRUD'])
def leer_tareas():
    return {"Las tareas registradas son: ": tareas}
    