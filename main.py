from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel, select
from models.Product import Product, ProductRequest, ProductResponse
import os

app = FastAPI()

# Carregar variables d’entorn
load_dotenv()

# Configurar la connexió a la BD
DATABASE_URL= os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Creació de les taules a la BD
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# Esta bien
@app.post("/product", response_model=dict, tags=["CREATE PRODUCT"])
def add_product(product = ProductRequest, db:Session = Depends(get_db)):
    insert_product = Product.model_validate(product)
    db.add(insert_product)
    db.commit()
    return {"missatge":"Producte Afegit Correctament"}

# Esta bien
@app.get("/product/{id}", response_model=ProductResponse, tags=["GET PRODUCT BY ID"])
def get_product(id: int, db:Session = Depends(get_db)):
    comanda = select(Product).where(Product.id == id)
    resultat = db.exec(comanda).first()
    return ProductResponse.model_validate(resultat)

# no esta bien porque la ultima linia solo sirve para validar una linia pero le paso muchas
@app.get("/product", response_model=ProductResponse, tags=["GET ALL PRODUCTS"])
def get_products(db:Session = Depends(get_db)):
    comanda = select(Product)
    resultats = db.exec(comanda).all()
    return ProductResponse.model_validate(resultats) # Retorno totes les dades menys les sensibles :
                                                     # el nom i contacte del proveïdor

# no esta bien porque la ultima linia solo sirve para validar una linia pero le paso muchas
@app.get("/api/product/{nom}", response_model=ProductResponse, tags=["GET PRODUCTS BY A CAMP"])
def get_product_camp(nom: str, db:Session = Depends(get_db)):
    comanda = select(Product).where(Product.nom == nom)
    resultats = db.exec(comanda).all()
    return ProductResponse.model_validate(resultats) # Retorno totes les dades menys les sensibles :

# Esta bien
@app.delete("/product/{id}", response_model=dict, tags=["DELETE PRODUCT BY ID"])
def delete_product(id : int, db:Session = Depends(get_db)):
    comanda = select(Product).where(Product.id == id)
    resultat = db.exec(comanda).first()
    db.delete(resultat)
    db.commit()
    return {"missatge":"Producte Eliminat Correctament"}

# Esta bien pero hace falta hacer preguntas de las dudas
@app.get("/api/product/{id}", response_model=ProductRequest, tags=["GET A PARTIAL PRODUCT"])
def get_product_partial(id: int, db:Session = Depends(get_db)):
    comanda = select(Product).where(Product.id == id)
    resultat = db.exec(comanda).first()
    return ProductRequest.model_validate(resultat) # Retorno totes les dades menys les sensibles :