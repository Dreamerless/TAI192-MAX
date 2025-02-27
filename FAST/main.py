from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken

app = FastAPI(
    title='Mi primerAPI 192',
    description='Acosta Gonzalez Maximiliano',
    version='1.0.1'
)

# BD ficticia
usuarios = [
    {"id": 1, "nombre": "miguel", "edad": 24, "correo": "miguel@gmail.com"},
    {"id": 2, "nombre": "fer", "edad": 32, "correo": "fer@gmail.com"},
    {"id": 3, "nombre": "carmelo", "edad": 58, "correo": "carmelo@gmail.com"},
    {"id": 4, "nombre": "frida", "edad": 17, "correo": "frida@gmail.com"}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'Hello World'}

# Endpoint Autentificacion
@app.post('/auth/', response_model=modeloAuth, tags=['Autentificacion'])
def login(autorizacion: modeloAuth):
    if autorizacion.email == 'usuario@mail.com' and autorizacion.passw == '123456789':
        token: str = createToken(autorizacion.model_dump())
        print(token)  # Corregido el error tipográfico
        return JSONResponse(content={"token": token})  # Devuelve el token en un JSON válido
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")  # Manejo de credenciales incorrectas

# Endpoint CONSULTA TODOS
@app.get('/TodosUsuarios', response_model=List[modeloUsuario], tags=['Operaciones CRUD'])
def leerUsuarios():
    return usuarios

# Endpoint Agregar nuevos
@app.post('/usuarios/', response_model=modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuarios(usuario: modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario.model_dump())
    return usuario

# Endpoint Actualizar
@app.put('/usuarios/{id}', response_model=modeloUsuario, tags=['Operaciones CRUD'])
def actualizarUsuarios(id: int, usuarioActualizado: modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

# Endpoint Eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminarUsuarios(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Los usuarios existentes restantes son": usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")