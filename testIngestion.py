from app.ingestion import extractContentFromPDF
# from app.ingestion import getWordCount
from app.chunking import chunkText
from app.embeddings import createEmbeddingsForChunks
from app.embeddings import createEmbeddingForTheQuestion
from app.retreival import selectTop3ChunksWithHighestSimilarityScores
from app.generation import generateAnswers
from app.vectorStore import storeEmbeddings
from app.vectorStore import retrieveFromVectorStore
pdfPath = "Documents/RAG_Document_1_Python.pdf"


# allWords = getWordCount(pdfPath)
# print(allWords)

pages = extractContentFromPDF(pdfPath) #it returns a list of dictionaries
print("This is how the pages look like -  ", pages)




allChunks = chunkText(pages)
print("All the chunks together ~ \n\n")
print(allChunks)





chunkEmbeddings = createEmbeddingsForChunks(allChunks)
print("\n----------Embeddings for Chunks------------\n")
print("\n----FirstEmbedding------\n")
print(chunkEmbeddings[0])
print("\n--------SecondEmbedding---------------\n")
print(chunkEmbeddings[1])


#Store the embeddings here ~
storeEmbeddings(chunkEmbeddings, allChunks)



question = "Tell me something about Python"
embeddedQuestion = createEmbeddingForTheQuestion(question) #One that you will recieve from the front end


#retrieval goes here

results = retrieveFromVectorStore(embeddedQuestion) #topK's default value is given as 3 in the function definition
contextChunks = results["documents"][0]

print("Retrieved IDs: ", results["ids"])
print("Retrieved Documents: ", results["documents"])
print("Number of retrieved chunks: ", len(contextChunks))



# print("\n---------------------Printing the top-3 similarity Scores with the text that will be used as context--------------------\n")

# contextChunks = []
# for result in results:
#     print("chunkNumber: ", result["chunkNumber"])
#     print("source: ", result["source"])
#     print("score: ", result["score"])
#     chunk = allChunks[result["chunkNumber"]]
#     print("text: ", chunk["text"])
#     contextChunks.append(chunk["text"])
  

context = "\n\n".join(contextChunks)

#Now we will generate an answer - 
print("\n------------This is the context that we are passing onto the LLM ~ ----------------------------------------\n")
print(context)
answer = generateAnswers(question,context) 
print("This is the answer we get from the LLM : \n\n", answer)

