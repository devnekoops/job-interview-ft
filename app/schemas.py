from typing import List, Optional

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str

class Checksum(BaseModel):
    token: str

class Flag(BaseModel):
    flags: str