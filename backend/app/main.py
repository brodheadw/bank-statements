from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

from workers.tasks import parse_bank_statement
from workers.celery_worker import celery_app

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
        
        task = parse_bank_statement.delay(file_location)

        return {"filename": file.filename,
                "message": "File uploaded: parsing started",
                "task_id": task.id}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "An error occurred while uploading the file.", "error": str(e)})
    
@app.get("/status/{task_id}")
def task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result
        }
    else:
        response = {
            'state': task.state,
            'error': str(task.info)  # this is the exception raised
        }
    return JSONResponse(content=response)

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "healthy"})
@app.on_event("startup")
def startup_event():
    # This is where you can initialize any resources or connections
    print("Starting up the FastAPI application...")
@app.on_event("shutdown")
def shutdown_event():
    # This is where you can clean up any resources or connections
    print("Shutting down the FastAPI application...")
# This is a simple FastAPI application that allows users to upload bank statement files.
# The files are saved to a specified directory, and a Celery task is triggered to parse the file.
# The application also provides endpoints to check the status of the parsing task and a health check endpoint.
