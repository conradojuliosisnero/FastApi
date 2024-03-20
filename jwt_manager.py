from jwt import encode

# funcion para creacion del tokent 
def create_token(data: dict):
    token = encode(payload=data, key="my_secret_key",algorithm="HS256")
    return token