
import asyncio
import time
import traceback
import uvicorn

from propiedadDeLosAlpes.modulos.agente.api import v1

from propiedadDeLosAlpes.modulos.agente.infraestructura.consumidores import suscribirse_a_topico

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


app.include_router(v1, prefix="/v1", tags=["Version 1"])
