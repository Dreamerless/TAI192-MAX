from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Gabriel Manzano Ruíz',
    version= '1.0.1'
)

usuarios=[
    {"id": 1,"nombre":"ivan", "edad":37},
    {"id": 2, "nombre":"isay", "edad":15},
    {"id": 3, "nombre":"luis", "edad":18},
    {"id": 4, "nombre":"ana", "edad":37}
]

#Endponit home

@app.get('/', tags=['Mi calificación tai api'])
def home():
    return {'messaje':'Hello World'}

#Endpoint CONSULTA TODOS
@app.get('/todosUsuarios', tags =['Operaciones CRUD'])
def leerUsuarios():
    return{"Los usuarios registrados son ":usuarios}

#Endpoint Agregar Nuevos Usuarios
@app.post('/ususario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
        for usr in usuarios:
            if usr["id"] == usuario.get("id"):
                raise HTTPExeption(status_code=400, detail="El id ya esxiste")

                usuarios.append(usuario)
                return usuario
                
#Endpoint parámetro obligatorio
@app.get('/usuario/{id}', tags=['Parámetro Obligatorio id'])
def consultaUsuario(id: int):
    #Simulación de base de datos
    #consulta = select * from usuario where id = id
   return{'Se encontro el usuario con el id':id}


@app.get("/usuario/", tags=["Parámetro Opcional"])
def consultaUsuario2(id: Optional[int] = None):

    if id is not None:
        for usu in usuarios:
            if usu['id'] == id:
                return {"mensaje":"Usuario encontrado", "usuario:": usu}
        return {"mensaje":f"No se encontro el usuario con id: {id}"}
    else:
        return {"mensaje":"No se proporciono un id"}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}