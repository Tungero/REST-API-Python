# to use this module type in cmd:
# pip install requests
import requests

def get(ID=None):
    id_ = "" if ID == None else f"/{ID}"
    req = requests.get("http://localhost:5000/movies" + id_)
    return req.text

def post(title, description, release_year):
    req = requests.get("http://localhost:5000/movies", json=data)    
    return req.text

def put(id, data):
    req = requests.get(f"http://localhost:5000/movies/{id}", json=data)    
    return req.text


# edit the variable below to edit the body of your request
data = {
        'title': "some movie",
        'description': "some description",
        'release_year': 1992,
    }

print(get())

#print(post(data))

#print(put(14, data)


