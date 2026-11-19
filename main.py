from fastapi import FastAPI
from fastapi import UploadFile, File, HTTPException
import shutil
import os
from pydantic import BaseModel

from app.embeddings import createEmbeddingForTheQuestion
from app.vectorStore import retrieveFromVectorStore
from app.generation import generateAnswers
from app.pipeline import processPDF
app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def healthCheck():
    return {"Status": "Sirius is Running"}

@app.post("/ask")
def askAQuestion(request : QuestionRequest):
    question = request.question
    embeddedQuestion = createEmbeddingForTheQuestion(question)
    #Now use chromaDB to get the results
    results = retrieveFromVectorStore(embeddedQuestion) #default topk = 3
    contextChunks = results["documents"][0]
    context = "\n\n".join(contextChunks)
    answer = generateAnswers(question, context)

    return{
        "Question: " : question,
        "Answer: ": answer

    }


@app.post("/upload")
async def uploadPDF(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDFs are to be uploaded" 
        )
    os.makedirs("Documents", exist_ok=True)
    pdfPath = os.path.join("Documents", file.filename)
    try:
        with open(pdfPath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        chunkCount = processPDF(pdfPath)

        return {
            "message": "PDF processed succesfully",
            "filename": file.filename,
            "chunks_created": chunkCount
        }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))
    finally:
        await file.close() 
