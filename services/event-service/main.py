from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.adapters.routers.event_router import router
from src.core.config import get_env_var

app = FastAPI(
    title="Event Service API",
    version="1.0.0",
    description="Serviço de gerenciamento de usuários para o sistema de bilhetagem.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas da API
app.include_router(router, tags=["Events"])


@app.get("/")
def root():
    return {"message": "Event Service está rodando! 🚀"}


if __name__ == "__main__":
    import uvicorn

    port = get_env_var("API_PORT")
    uvicorn.run("main:app", host="0.0.0.0", port=int(port), reload=True)
