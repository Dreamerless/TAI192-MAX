from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title='mi primer api',
    description= 'Acosta Gonzalez Maximiliano',
    version='1.0.1'
)

usuarios = [
    {"id": 1, "nombre": "Alfredo", "edad": 21},
    {"id": 2, "nombre": "Polo", "edad": 22},
    {"id": 3, "nombre": "Pedro", "edad": 19},  
    {"id": 4, "nombre": "Maria", "edad": 20}
]

#endPoint home

@app.get('/')
def home():
    return {'hello':'world FastAPI'}

#endpoint consulta todos
@app.get('/todosUsuarios', tags=['operaciones CRUD'])
def leerUsuarios():
    return {"Los usuarios registrados son: ": usuarios}

#endpoint Añadir
@app.post('/addUsuarios/', tags=['operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"]== usuario.get("id"):
            raise HTTPException(status_code=400, detail="Id existente")
    usuarios.append(usuario)
    return usuario

#endpoint actualizar
@app.put('/actualizarUsuarios/{id}', tags=['operaciones CRUD'])
def actualizarUsuario(id:int, usuario:dict):
    for index,usr in enumerate(usuarios):
        if usr["id"]== id:
                usuarios[index].update(usuario)
                return usuarios(index)
    raise HTTPException(status_code=400, detail="Id inexistente")

# Endpoint para eliminar un usuario
@app.delete("/eliminarUsuarios/{id}", tags=["operaciones CRUD"])
def eliminar_usuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr.id == id:
            del usuarios[index]
            return {"message": "Usuario eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Usuario no encontrado")