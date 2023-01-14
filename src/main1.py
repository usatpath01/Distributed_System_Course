# Tutorial on Pydantic BaseMode
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel # All the feild or data will be inherited from BaseModel 

#Basically everything is going to be inhherited from this basemodel
class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None #Default value is 'None'

app = FastAPI()

# post inserts the data
@app.post("/package/")
async def make_package(package: Package):
    return package