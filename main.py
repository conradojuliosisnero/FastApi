from fastapi import FastAPI,Body,Path,Query,Request,HTTPException,Depends
from fastapi.security import HTTPBearer
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,List
from jwt_manager import create_token, validate_token
from config.database import Sesion,engine,Base
from models.movie import Movie

app = FastAPI();
app.title = 'Web Movies'
app.version = '0.0.1'

Base.metadata.create_all(bind=engine)

class JWTBearer(HTTPBearer):
    async def __call__(self,request:Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403,detail="credential error")

class user(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5,max_length=15)
    overview:str = Field(min_length=15,max_length=50)
    year:int = Field(le=2024)
    rating: float = Field(ge=1,le=10)
    category: str = Field(min_length=5,max_length=15)
    class Config:
        json_schema_extra = {
					"example": {
						"id": 1,
						"title": "Mi pelicula",
						"overview": "ASD123456",
						"year": 2022,
						"rating": 9.8,
						"category": "Acción"
					}
				}

# peliculas 
movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "accion"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "accion"
	},{
		"id": 3,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "accion"
	},{
		"id": 4,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "accion"
	}
]

# ruta principal 
@app.get('/',tags=['home'])
def get_message():
  return "Hello World from FastApi"

# ruta de login 
@app.post('/login',tags=['authentication'])
def login_user(user: user):
    if user.email == "admin@gmail.com" and user.password == "1234":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200,content=token)

# metodo get 
@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
	return JSONResponse(status_code=200,content=movies)

# metodo get por id 
@app.get('/movies/{id}',tags=['movies'],response_model=Movie,status_code=200)
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404,content=[])

# metodo get por categorias 
@app.get('/movies/',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movie_by_category(category: str = Query(min_length=5,max_length=15)) -> List[Movie]:
	data = [item for item in movies if item['category'] == category ]
	return JSONResponse(status_code=200,content=data)

# metodo post 
@app.post('/movies',tags=['movies'],response_model=dict,status_code=201) 
def create_movie(movie: Movie) -> dict:
	movies.append(movie)
	return JSONResponse(status_code=201,content={"message": "register movie succesfull"})

# metodo put 
@app.put('/movies{id}',tags=['movies'],response_model=dict,status_code=200)
def update_movie(id: int,movie: Movie) -> dict:
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return JSONResponse(status_code=200,content={"message": "modify movie succesfull"})

# metodo delete 
@app.delete('/movies{id}',tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(status_code=200,content={"message": "delete movie succesfull"})
			