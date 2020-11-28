# -*- coding: utf-8 -*-

from fastapi import FastAPI

from data import products

app = FastAPI()

@app.get('/names')
async def getnames():
    arr_data= []
    for idx in range(0, len(products)):
        item_data = products[idx].get("name")
        arr_data.append(item_data)
    return  arr_data


@app.get('/')
async def home_page(): 
    return {"data": products}


@app.post('/home/{item_id}')
async def post_item(item_id:str ):
    arr_data= []
    for idx in range(0, len(products)):
        item_data = products[idx].get(item_id)
        arr_data.append(item_data)
    return  arr_data

