from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db, CategoryBase,LocalSession
from models import CategoryModel
from schemas import CategoryResponse

app = FastAPI(title="FastAPI MSSQL Integration")

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/products", response_model=List[CategoryResponse])
def read_all_products(db: Session = Depends(get_db)):
    """Fetch all rows from the pre-existing Products table."""
    products = db.query(CategoryModel).all()
    return products

#@app.post("/category/add",response_model = CategoryResponse)
#def createcategory(categoroy :CategoryBase, db: Session = Depends(get_db)):