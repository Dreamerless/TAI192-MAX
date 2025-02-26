from pydantic import BaseModel, Field

class modeloUsuario(BaseModel):
    id:int = Field(...,gt=0, description="Solo 1 ID positivos")
    nombre:str = Field(...,min_length=3, max_length=85, description="Solo letras min 3 max 85")
    edad:int = Field(...,gt=0,lt=125)
    correo:str = Field(..., example="usuario@gmail.com", pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
