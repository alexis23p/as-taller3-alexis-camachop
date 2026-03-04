from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AS-Taller3 API (scaffold)")


@app.get('/health')
def health():
    return {"status": "ok"}


@app.post('/users/register', response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail='Username already registered')
    db_user = crud.create_user(db, user)
    return db_user


@app.get('/products', response_model=list[schemas.ProductOut])
def list_products(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)


@app.post('/products', response_model=schemas.ProductOut)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@app.post('/cart/{user_id}/add')
def add_item_to_cart(user_id: int, item: schemas.CartItemBase, db: Session = Depends(get_db)):
    cart = crud.add_to_cart(db, user_id, item.product_id, item.quantity)
    return {"cart_id": cart.id}
