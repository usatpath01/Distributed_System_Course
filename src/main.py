# helps us to find what type something is 
from typing import Optional

# import fasiapi class because we need to import all the necessary functionality
from fastapi import FastAPI

# create instance of fastapi app, this will interact with all the things in api
# let's keep the instance name as app (Most common name :P)
app = FastAPI()

# http method get to read the data - it handles the get method for the url app.get
# here the url mean '/'

@app.get('/')

# let's create a async for asynhronous (not 100% required but just for better practice)
async def hello_world():
    #returning a dictionary to json response
    return {"Hello":"World"}
     
