from typing import Union
from fastapi import FastAPI
from encryptor import Encryptor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/encrypt/{key}/{text}")
async def encrypt(key: str, text: Union[str, None] = None):

    encryptor = Encryptor(key)
    encrypted_text = await encryptor.encrypt(text)
    
    return encrypted_text


@app.get("/decrypt/{key}/{encrypted_text}")
async def decrypt(key: str, encrypted_text: Union[str, None] = None):
    
    encryptor = Encryptor(key)
    decrypted_text = await encryptor.decrypt(encrypted_text.encode())
    return decrypted_text



