from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Header
import hashlib
from . import schemas

app = FastAPI()


@app.post("/login", response_model=schemas.Checksum)
def login(user: schemas.Login):

    hash_obj = hashlib.new("SHA1")
    hash_obj.update((user.username+user.password).encode("utf-8"))
    digest = hash_obj.hexdigest()
    return {"token": digest}


@app.post("/flag")
def login(flag: schemas.Flag):
    print(flag.flag)
    return {"status": "ok"}

