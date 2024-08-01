from fastapi import APIRouter,FastAPI
from routes.user import user
from routes.chatbot import chatbot
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
import uvicorn
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)
app = FastAPI()
prefix_router = APIRouter(prefix="/chatrap")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.mount("/chatrap/static/images", StaticFiles(directory="static/images"), name="images")
app.mount("/static/images", StaticFiles(directory="static/images"), name="static/images")

app.include_router(user.router, prefix="/user", tags=["users"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=12849)

