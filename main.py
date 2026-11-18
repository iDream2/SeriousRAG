from fastapi import FastAPI
from pydantic import BaseModel
from app.embeddings import createEmbeddingForTheQuestion
from app.vectorStore import retrieveFromVectorStore
from app.generation import generateAnswers
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

