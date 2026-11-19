from app.ingestion import extractContentFromPDF
from app.chunking import chunkText
from app.embeddings import createEmbeddingsForChunks
from app.embeddings import createEmbeddingForTheQuestion
# from app.retreival import selectTop3ChunksWithHighestSimilarityScores
# from app.generation import generateAnswers
from app.vectorStore import storeEmbeddings
# from app.vectorStore import retrieveFromVectorStore

def processPDF(pdfPath):
    pages = extractContentFromPDF(pdfPath)

    allChunks = chunkText(pages)

    chunkEmbeddings = createEmbeddingsForChunks(allChunks)

    storeEmbeddings(chunkEmbeddings, allChunks)

    return len(allChunks)
