from sqlalchemy.orm import Session
from database import SessionLocal
from models import LlmTable

def seed_data(db: Session):
    users = [
        LlmTable(id=1, llm_type="openai"),
        LlmTable(id=2, llm_type="gemini"),
        LlmTable(id=3, llm_type="mistral"),
        LlmTable(id=4, llm_type="gemma"),
        LlmTable(id=5,llm_type ="tavily"),
        LlmTable(id=6, llm_type="dalle")
    ]
    db.add_all(users)
    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_data(db)
    except Exception as e:
        db.rollback()
    finally:
        db.close()
