from jwt import encode,decode

# funcion para creacion del tokent 
def create_token(data: dict):
    token = encode(payload=data, key="my_secret_key",algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data:dict = decode(token,key="my_secret_key",algorithms=['HS256'])
    return data