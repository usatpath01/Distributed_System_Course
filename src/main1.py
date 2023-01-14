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

# To combine BaseModel with path parameters
@app.post("/package1/{package_priority}")
async def make_package(package_priority: int, package: Package, value: bool):   # To set the priority of the package 
    return {"package_priority": package_priority, **package.dict(), "value": value} 
    # Two astrick for dictionary