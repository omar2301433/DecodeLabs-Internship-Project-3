from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, crud, schemas
from database import engine, SessionLocal
from auth import create_access_token
from auth import get_current_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    result = crud.create_user(db, user)
    if not result:
        raise HTTPException(status_code=400, detail="Email already exists")
    return result




@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user.email, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user.id)})

    return {"access_token": token, "token_type": "bearer"}




@app.get("/protected")
def protected_route(user_id: str = Depends(get_current_user)):
    return {
        "message": "You are authenticated!",
        "user_id": user_id
    }