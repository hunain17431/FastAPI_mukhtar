from fastapi import FastAPI

app = FastAPI()

usuaris = [{"id": 1,"nom": "hunain","edad": 19}, # Creem la llista d'usuaris amb un d'exemple
           {"id": 2,"nom": "niko","edad": 18},
           {"id": 3,"nom": "ibai","edad": 16}]


@app.post("/api/users")
async def crear_objecte(id_user: int,nom : str,edad: int,):
    user = {"id": id_user,"nom": nom,"edad": edad}  # Creem un diccionari amb les dades de l'usuari
    usuaris.append(user)    # Afegim l'usuari a la llista d'usuaris
    return {"usuaris": usuaris}   # Retornem un diccionari amb tots els d'usuaris

@app.get("/api/users/{id}")
async def consultar_usuari(id: int):
    for user in usuaris: # Recorrem la llista dels usuaris
        if user["id"] == id: # Comprovem si hi ha algun usuari amb el mateix id que hem rebut
            return {"usuari": user} # En cas que trobem algun usuari el retornem
    return{} # Si no hem trobat cap usuari retornem un diccionari buit

@app.get("/api/users")
async def consultar_usuaris():
    return {"usuaris": usuaris}  # Retornem tots els usuaris

@app.put("/api/users/{id}")
async def actualitzar_usuaris(id: int,nom: str,edad: int):
    for usuari in usuaris: # Recorrem la llista dels usuaris
        if usuari["id"] == id:  # Comprovem si hi ha algun usuari amb el mateix id que hem rebut
            usuari["nom"] = nom # Si el trobem actualitzem les dades anteriors amb les noves dades rebudes
            usuari["edad"] = edad
            return{"Usuaris": usuaris}  # Retornem tots els usuaris actualitzats en forma de diccionari
    return{"Usuari": "No hi ha cap usuari amb aquest id"}  # Si no trobem l'usuari retornem un missatge

