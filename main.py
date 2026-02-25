from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Importamos tu lógica de negocio existente
from Usuario import CAsunto

app = FastAPI(title="API de Comentarios Clientes")

# Configuración de CORS (Indispensable para React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos (Esquema de lo que recibe la API)
class ComentarioSchema(BaseModel):
    asunto: str
    comentario: str

# --- RUTAS DEL CRUD ---

@app.get("/comentarios")
def listar_comentarios():
    try:
        # Llamamos a tu método existente 
        registros = CAsunto.mostrarAsunto() 
        # Convertimos las tuplas de MySQL a Diccionarios para JSON
        return [{"id": r[0], "asunto": r[1], "comentario": r[2]} for r in registros]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/comentarios")
def crear_comentario(data: ComentarioSchema):
    try:
        CAsunto.ingresarAsunto(data.asunto, data.comentario) [cite: 3]
        return {"status": "success", "message": "Comentario guardado"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/comentarios/{id}")
def actualizar_comentario(id: int, data: ComentarioSchema):
    try:
        CAsunto.editarAsunto(id, data.asunto, data.comentario) [cite: 3]
        return {"status": "success", "message": "Comentario actualizado"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/comentarios/{id}")
def borrar_comentario(id: int):
    try:
        CAsunto.eliminarAsunto(id) [cite: 3]
        return {"status": "success", "message": "Comentario eliminado"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))