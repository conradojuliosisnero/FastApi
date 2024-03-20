from fastapi import FastAPI,Body,Path,Query
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,List

app = FastAPI();
app.title = 'Web Movies'
app.version = '0.0.1'

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

# metodo get 
@app.get('/movies',tags=['movies'],response_model=List[Movie])
def get_movies() -> List[Movie]:
	return JSONResponse(content=movies)

# metodo get por id 
@app.get('/movies/{id}',tags=['movies'],response_model=Movie)
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])

# metodo get por categorias 
@app.get('/movies/',tags=['movies'],response_model=List[Movie])
def get_movie_by_category(category: str = Query(min_length=5,max_length=15)) -> List[Movie]:
	data = [item for item in movies if item['category'] == category ]
	return JSONResponse(content=data)

# metodo post 
@app.post('/movies',tags=['movies'],response_model=dict) 
def create_movie(movie: Movie) -> dict:
	movies.append(movie)
	return JSONResponse(content={"message": "register movie succesfull"})

# metodo put 
@app.put('/movies{id}',tags=['movies'],response_model=dict)
def update_movie(id: int,movie: Movie) -> dict:
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return JSONResponse(content={"message": "modify movie succesfull"})

# metodo delete 
@app.delete('/movies{id}',tags=['movies'],response_model=dict)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "delete movie succesfull"})
			