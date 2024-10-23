from fastapi import FastAPI, HTTPException
import db_alumnat
from alumne import alumnes_schema, alumne_schema
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AlumneModel(BaseModel):
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: int
    Grup: int

class tablaAlumne(BaseModel):
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    DescAula: str


@app.get("/")
def read_root():
    return {"Api d'Alumnes"}

@app.get("/alumne/list", response_model=List[tablaAlumne])
def read_alumnes():
    alumnes = db_alumnat.read_alumnes()

    if not alumnes:
        raise HTTPException(status_code=404, detail="No s'han trobat alumnes")

    return alumnes_schema(alumnes)

@app.get("/alumne/show/{id}", response_model=dict)
def read_alumne(id: int):
    alumne = db_alumnat.read_alumne_by_id(id)

    if not alumne:
        raise HTTPException(status_code=404, detail="Estudiant no trobat")

    return alumne_schema(alumne)

@app.post("/alumne/add")
def add_alumne(alumne: AlumneModel):
    
    aula = db_alumnat.read_aula_by_id(alumne.IdAula)
    
    if aula is None:
        raise HTTPException(status_code=404, detail="No s'ha trobat l'aula")

    
    new_alumne = db_alumnat.create_alumne(
        alumne.IdAula, 
        alumne.NomAlumne, 
        alumne.Cicle, 
        alumne.Curs, 
        alumne.Grup
    )

    return {"message": "S'ha afegit correctament", "alumne": new_alumne}

@app.put("/alumne/update/{id}")
def update_alumne(IdAlumne:int,curs:int):
    updated_records = db_alumnat.update_alumne(IdAlumne,curs)
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="Items to update not found")
    
    alumne = db_alumnat.read_alumne_by_id(IdAlumne)
    if not alumne:
        raise HTTPException(status_code=404, detail="Estudiant no trobat")

    return "S'ha modificat correctament",alumne_schema(alumne)
    
@app.delete("/alumne/delete/{id}")
def delete_alumne(IdAlumne:int):
    deleted_records = db_alumnat.delete_alumne(IdAlumne)
    if deleted_records == 0:
       raise HTTPException(status_code=404, detail="Items to delete not found")
    return "S'ha esborrat correctament"

@app.get("/alumne/listAll/{IdAlumne}")
def get_all_alumnes(IdAlumne: int):
    try:
        alumnes = db_alumnat.list_all_alumnes(IdAlumne)
        if not alumnes:
            raise HTTPException(status_code=404, detail="No alumnes found")
        return alumnes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching alumnes: {e}")