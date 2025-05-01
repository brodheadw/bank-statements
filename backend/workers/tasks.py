from workers.celery_worker import celery_app

@celery_app.task
def parse_bank_statement(filepath):
    # For now, dummy parser
    print(f"Parsing file: {filepath}")
    return {"status": "Parsed successfully", "file": filepath}