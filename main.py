from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Optional

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
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},{
		"id": 3,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},{
		"id": 4,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]


@app.get('/',tags=['home'])
def get_message():
  return "Hello World from FastApi"

# metodo get 
@app.get('/movies',tags=['movies'])
def get_movies():
	return movies

# metodo get por id 
@app.get('/movies{id}',tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

# metodo get por categorias 
@app.get('/movies/',tags=['movies'])
def get_movie_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category ]

# metodo post 
@app.post('/movies',tags=['movies']) 
def create_movie(movie: Movie):
	movies.append(movie)
	return movies

# metodo put 
@app.put('/movies{id}',tags=['movies'])
def update_movie(id: int,movie: Movie):
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return movies

# metodo delete 
@app.delete('/movies{id}',tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
			