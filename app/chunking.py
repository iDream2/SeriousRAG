allChunks = [] #We'll store the chunk and the document and the page number it was taken from
def chunkText(pages,chunkSize=50,overlap=10): #These are default values, we'll get pages from ingestion.py. Pages is a list of dictionaries. Although our documents are of one page, so they have only one dictionary inside a list.
    stepSize = chunkSize - overlap
    

    for page in pages: #So, this will only be on iteration
        
        words = page["text"].split() #split the whole text into a list of words
        print("\n---------------------The words in a page-----------------------------\n", words)
        for start in  range(0, len(words), stepSize):
            
            end = start + chunkSize
            chunkWords = words[start:end] #Breaking the words list into a list of chunkWords
            print("\n-----------------------This is chunkWords at every iteration: --------------------------\n", chunkWords)
            
            if not chunkWords:
                continue
            chunkText = " ".join(chunkWords)# Making the chunkWords into a complete string for each chunk
            
            
            allChunks.append({
                "source": page["source"],
                "page": page["page"],
                "text": chunkText
            })


    return allChunks
        
    