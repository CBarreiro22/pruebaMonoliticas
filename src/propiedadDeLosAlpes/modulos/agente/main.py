
import asyncio
import time
import traceback
from agente.infraestructura.v1.eventos import PropiedadRegistrada
import uvicorn

from agente.api import v1

from agente.infraestructura.consumidores import suscribirse_a_topico

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-propiedad-registrada", "sub-agente", EventoPropiedad))
    tasks.append(task1)


@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/prueba-propiedad-registrada", include_in_schema=False)
async def prueba_propiedad_registrada() -> dict[str, str]:
    payload = PropiedadRegistrada(id_propiedad="12345", campos_faltantes=["campo1", "campo2"])

    evento = EventoPropiedad(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=UsuarioValidado.__name__,
        usuario_validado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-propiedad-registrada")
    return {"status": "ok"}

app.include_router(v1, prefix="/v1", tags=["Version 1"])
