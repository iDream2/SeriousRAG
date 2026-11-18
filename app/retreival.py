#Using Cosine Similarity or some other metrics we will now determine the most relevant document for answering.
import numpy as np


def selectTop3ChunksWithHighestSimilarityScores(embeddedQuestion,chunkEmbeddings): #question we will get from the front-end
        similarityScores = []
        for embeddedChunk in chunkEmbeddings:
                embeddedValues = embeddedChunk["embeddings"]
                chunkNumber = embeddedChunk["chunkNumber"]
                similarityScore = np.dot(embeddedQuestion, embeddedValues)/(np.linalg.norm(embeddedValues)*np.linalg.norm(embeddedQuestion)) #Can't remember the formula 
                similarityScores.append({
                        "chunkNumber":chunkNumber,
                        "source":embeddedChunk["source"],
                        "page": embeddedChunk["page"],
                        "score":similarityScore
                })
        
        reverseSortedSimilarityScores = sorted(similarityScores, key=lambda x: x['score'], reverse=True)
        return [reverseSortedSimilarityScores[0],reverseSortedSimilarityScores[1],reverseSortedSimilarityScores[2]]