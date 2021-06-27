from fastapi import FastAPI
from fastapi import UploadFile , File
import uvicorn
from fastapi.encoders import jsonable_encoder
from stock import *
from pydantic import BaseModel
from typing import Optional





class Item(BaseModel):
    ticker: str
    preddays: str
    epochs : Optional[int] = 2




app = FastAPI()





@app.post('/')
async def predict_image(item:Item):
        setparam(item.epochs)
        print(item.epochs)
        print(item.preddays)
        createdata = create_data(item.ticker,int(item.preddays))
        modeltrain = train(createdata,item.epochs)
        result =  str(predict(createdata))


        return result

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')



