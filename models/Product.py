from sqlmodel import SQLModel, Field

# Model principal amb tota la informació del producte
class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True) # id auto incrementable
    nom: str
    descripcio: str
    preu: float
    nom_proveidor: str | None = None # Dada sensible
    contacte_proveidor: str | None = None # Dada sensible

# Model per crear un producte, no conté les dades sensibles
class ProductRequest(SQLModel):
    nom: str
    descripcio: str
    preu: float

# Model per retornar producte a l'usuari
class ProductResponse(SQLModel):
    id: int
    nom: str
    descripcio: str
    preu: float