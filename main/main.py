from typing import List
from fastapi import FastAPI, HTTPException, status
from models import MobilePhone, OsType
from database import all_phones

app = FastAPI()


# Function to get the current maximum ID in the data
def get_max_id():
    if not all_phones:
        return 0
    return max(phone.Id for phone in all_phones)


@app.get("/")
async def root():
    return {"message": "REST-based application which can store and present information about mobile phones"}


@app.get("/phone_store/")
async def get_all_phones():
    return all_phones;


@app.get("/phone_store/{phone_id}")
async def get_mobile_phone(phone_id: int):
    if phone_id < 0:
        raise HTTPException(status_code=400, detail="Bad Request - otherwise")
    if phone_id > get_max_id():
        raise HTTPException(status_code=404, detail="Id is not in the database")
    return all_phones[phone_id - 1];



@app.post("/phone_store/")
async def add_phone(phone: MobilePhone):
    # Check if the provided ID is negative
    if phone.Id is not None and phone.Id < 0:
        raise HTTPException(status_code=400, detail="ID must be a non-negative integer")
    
    # Check if the ostype is among the allowed enums
    if phone.OS not in OsType:
        raise HTTPException(status_code=400, detail="Invalid operating system type. Allowed values are: android, ios, windows, other")

    # Convert all_phones from list of MobilePhone objects to list of dictionaries
    all_phones_dict = [p.dict() for p in all_phones]

    # Check if a phone with the same name and brand already exists
    existing_phone = next((p for p in all_phones_dict if p["Name"] == phone.Name and p["Brand"] == phone.Brand), None)
    if existing_phone:
        # Phone with the same name and brand exists
        raise HTTPException(status_code=409, detail="Phone is already in the database")
    else:
        # Phone does not exist, create a new one
        if phone.Id is not None:
            # Check if the provided ID already exists in the data
            if any(p["Id"] == phone.Id for p in all_phones_dict):
                raise HTTPException(status_code=409, detail="ID already exists")
        else:
            # Assign the next available ID in the sequence
            phone.Id = get_max_id() + 1
        all_phones.append(phone)  # Append the MobilePhone object directly (not as a dictionary)
        return phone
    

@app.delete("/phone_store/{phone_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_phone(phone_id: int):
    if phone_id < 0:
        raise HTTPException(status_code=400, detail="Bad Request - otherwise")
    if phone_id > get_max_id():
        raise HTTPException(status_code=404, detail="Id is not in the database")
    for phone in all_phones:
        if phone.Id == phone_id:
            all_phones.remove(phone)
            return
    raise HTTPException(status_code=404, detail="Id is not in the database")

