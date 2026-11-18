import chromadb
print("\n\n------------Inside the chromadb file----------------------\n\n")
client = chromadb.PersistentClient(path = "./chromadb")

print(f"\n\n The client is - {client} \n\n ")

collection = client.get_or_create_collection(
    name= "serious_rag"
)

print(f"\n\n The collection is - {collection} \n\n ")


def storeEmbeddings(chunkEmbeddings, allChunks):
    print("Status of allChunks in the chromaDB file: \n\n", allChunks)
    for chunk in chunkEmbeddings:
        chunkNumber = chunk["chunkNumber"]
        collection.add(
            ids = [ f"{chunk['source']}_{chunk['page']}_{chunk['chunkNumber']}" ],
            embeddings=[chunk["embeddings"]],
            documents = [allChunks[chunkNumber]["text"]], #The idea is that allChunks was enumerated at some point and we are using the chunkNumber as simply the positinal index as that is preserved later as well. We simply assigned increasing order of numbers to the chunks to identify them. 
            metadatas=[{
                "source": chunk["source"],
                "page":chunk["page"],
                "chunkNumber":chunk["chunkNumber"]
            }]
        )

    print(f"\n\nThis is the status of collection - {collection} \n\n")    
    print("Collection count: ", collection.count())



def retrieveFromVectorStore(questionEmbedding, topK=3):
    results = collection.query(
        query_embeddings=[questionEmbedding],
        n_results = topK
    )

    return results