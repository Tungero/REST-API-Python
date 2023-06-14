from flask import Flask, request, abort
import json

import movies

app = Flask(__name__)

@app.route("/")
def hello():
    return 'hello world'


@app.route("/movies", methods = ['GET'])
def get_movies():
    return json.dumps(movies.get(), indent=2)

@app.route("/movies/<int:id>", methods = ['GET'])
def get_movie(id):
    res = movies.get(id)

    if res == None:
        abort(404, f"Movie with id {id} not found.")
    
    return json.dumps(res, indent=2)

@app.route("/movies", methods = ['POST'])
def add_movie():
    data = request.json
    
    if 'title' not in data or 'release_year' not in data:
        abort(400, "Bad request. Missing title or release_year arguments")
    
    if type(data['release_year']) != int or not 10000 > data['release_year'] > 999:
        abort(400, "Bad request. release_year should be in format NNNN (4 numbers)")

    if 'description' not in data:
        data['description'] = ''
        
    if len(data) > 3:
        abort(400, "Bad request. Wrong format.")

    res = movies.add(data['title'], data['description'], data['release_year'])
    return json.dumps(res, indent=2)
    

@app.route("/movies/<int:id>", methods = ['PUT'])
def update_movie(id):
    data = request.json

    movie = movies.get(id)

    if movie == None:
        abort(404, f"Movie with id {id} not found.")

    if 'title' not in data or 'release_year' not in data:
        abort(400, "Bad request. Missing title or release_year arguments")
    
    if type(data['release_year']) != int or not 10000 > data['release_year'] > 999:
        abort(400, "Bad request. release_year should be in format NNNN (4 numbers)")
    
    if 'description' not in data:
        data['description'] = None

    if len(data) > 4:
        abort(400, "Bad request. Wrong format.")

    res = movies.update(movie['id'], data['title'], data['description'], data['release_year'])
    return json.dumps(res, indent=2)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
