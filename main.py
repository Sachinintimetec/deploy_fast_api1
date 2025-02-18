from typing import Optional

import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException,Body,Request
from pydantic import BaseModel
from mock_data_generator import generate_w9_mock_data  # Import the mock data generation function
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Directory to save uploaded files
UPLOAD_DIRECTORY = "uploaded_files"
# Ensure that the directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

class FormResponse(BaseModel):
    filename: str
    form_type: str
    data: dict  # Fields with their values and confidence scores
    
class Document(BaseModel):
    Bytes: str 


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload-form/")
async def upload_form(request: Request):
    try:
        body = await request.body()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"File upload failed: {str(e)}")
    mock_data = generate_w9_mock_data()
    # Return the mock response (adjust as needed for your actual use case)
    return {
        "filename": "uploaded_form.pdf",  # Placeholder filename
        # "form_type": form_type,
        "data": mock_data
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
