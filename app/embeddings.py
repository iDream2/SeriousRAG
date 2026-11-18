#The embedding function will recieve a list of dictionaries containing the chunks
from openai import OpenAI
from dotenv import load_dotenv
import os 




def createEmbeddingsForChunks(allChunks): #allChunks is a list of dictionaries
    allEmbeddings = []
    load_dotenv()
    client = OpenAI(api_key = os.getenv("OPEN_AI_KEY"))    
    print("\n==================Status of allChunks inside the embeddings file=============\n")
    print(allChunks)
    for number, chunk  in enumerate(allChunks): #iterating over every single dictionary in the list
        response = client.embeddings.create(
        model = "text-embedding-3-small",
        input = chunk["text"]
    )
        allEmbeddings.append(
            {
                "source" : chunk["source"],
                 "page" : chunk["page"],
                 "chunkNumber": number,
                 "embeddings" : response.data[0].embedding,
                 
            }
        )
    return allEmbeddings

def createEmbeddingForTheQuestion(question):
    load_dotenv()
    client = OpenAI(api_key = os.getenv("OPEN_AI_KEY")) 
    response = client.embeddings.create(
        model = "text-embedding-3-small",
        input = question
    )
    questionEmbedding = response.data[0].embedding
    return questionEmbedding