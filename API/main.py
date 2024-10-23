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


class Alumne(BaseModel):    #para convertir las respuesta a json
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

@app.get("/alumne/show/{id}", response_model=Alumne)
def read_alumnes_id(id:int):
    if db_alumnes.read_id(id) is not None:
        alumno = alumnes.alumne_schema(db_alumnes.read_id(id))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return alumno

@app.post("/alumnat/add")
def add_alumne(alumne: Alumne):
    
    aula = db_alumnes.read_aula_by_id(alumne.IdAula)
    
    if aula is None:
        raise HTTPException(status_code=404, detail="No s'ha trobat l'aula")

    
    new_alumne = db_alumnes.create_alumne(
        alumne.IdAula, 
        alumne.NomAlumne, 
        alumne.Cicle, 
        alumne.Curs, 
        alumne.Grup
    )

    return {"message": "S'ha afegit correctament", "alumne": new_alumne}

@app.put("/update_alumne/{IdAlumne}")
def update_alumne(IdAlumne:int,curs:int):
    updated_records = db_alumnes.update_alumne(IdAlumne,curs)
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="Items to update not found")
    
    alumne = db_alumnes.read_id(IdAlumne)
    if not alumne:
        raise HTTPException(status_code=404, detail="Estudiant no trobat")

    return "S'ha modificat correctament",alumnes.alumne_schema(alumne)
    
@app.delete("/delete_alumne/{IdAlumne}")
def delete_alumne(IdAlumne:int):
    deleted_records = db_alumnes.delete_alumne(IdAlumne)
    if deleted_records == 0:
       raise HTTPException(status_code=404, detail="Items to delete not found")
    return "S'ha esborrat correctament"

@app.get("/alumne/listAll/{IdAlumne}")
def get_all_alumnes(IdAlumne: int):
    try:
        alumnes = db_alumnes.list_all_alumnes(IdAlumne)
        if not alumnes:
            raise HTTPException(status_code=404, detail="No alumnes found")
        return alumnes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching alumnes: {e}")