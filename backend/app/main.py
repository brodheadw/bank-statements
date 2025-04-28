from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "/app/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Bank Statement Tracker is alive!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return JSONResponse(content={"filename": file.filename, "message": "File uploaded successfully."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "An error occurred while uploading the file.", "error": str(e)})