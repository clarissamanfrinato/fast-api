from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Crop(BaseModel):
    id: int
    name:str
    stage: int
    price: float
    description: str
    on_sale: bool

my_crops= [{
        'id': 1,
        'name': 'Blue Jazz',
        'stage': 1,
        'price': 35,
        'description': "The flower grows in a sphere to invite as many butterflies as possible.",
        'on_sale': True
}]

@app.get("/")
def root():
    return {"Hello World"}

@app.get("/crops/{id}")
def get_crops(id: int):

    for i in my_crops:
        if i['id'] == id:
            return i
        elif i['id'] not in my_crops:
            raise HTTPException(status_code=404, detail="Item not found.")


@app.post("/crops")
def create_crops(post: Crop):
    crop_dict= post.dict()
    crop_dict['id'] = '1'
    crop_dict['name'] = "Jazz Seeds"
    crop_dict['stage'] = 1
    crop_dict['price'] = 35
    crop_dict['description'] = "The flower grows in a sphere to invite as many butterflies as possible. banana"
    crop_dict['on_sale'] = True
    my_crops.append(crop_dict)
    return {crop_dict}