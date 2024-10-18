from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import db_alumnes
import alumnes

from typing import List

from pydantic import BaseModel

app = FastAPI()   #crea una instancia de api

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class alumne(BaseModel):    #para convertir las respuesta a json
    IdAlumne:int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    CreatedAt : str
    UpdateAt: str


class Aula(BaseModel):
    IdAULA: int
    DescAula: str
    Edifici: str
    Pis: str
    CreatedAt: int
    UpdateAt: int

class tablaAlumne(BaseModel):
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    DescAula: str  

   

@app.get("/")
def read_root():
    return {"Alumnat API"}
    

#@app.get("/alumnes/list", response_model=List[dict])
@app.get("/alumnes/list", response_model=List[tablaAlumne]) 
def read_alumnes():
    pdb= db_alumnes.read()
    alumnos_sch = alumnes.alumnes_schema(pdb)
    return alumnos_sch

@app.get("/alumne/show/{id}", response_model=alumne)
def read_alumnes_id(id:int):
    if db_alumnes.read_id(id) is not None:
        alumno = alumnes.alumne_schema(db_alumnes.read_id(id))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return alumno

#@app.post("/create_peli")
#async def create_film(data: film):
    titol = data.titulo
    any = data.fecha
    puntuacio = data.puntuacion
    vots = data.votos
    l_film_id = db_pelis.create(titol,any,puntuacio,vots)
    return {
        "msg": "we got data succesfully",
        "id film": l_film_id,
        "titol": titol
    }