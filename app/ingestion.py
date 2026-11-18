import fitz
import os

#Get word count of the pages just as a test ~
# def getWordCount(pdfPath):
#     #First we'll open the document
#     pdfDocument = fitz.open(pdfPath)
#     allWords = []
    
#     for page in pdfDocument:
#         pageTextWhole = page.get_text("text")
#         words = pageTextWhole.split()
#         print("The third word in this list is : ", words[2])  #Just to check
#         allWords.extend(words)    
        
#     print("Count of words is : ", len(allWords))        
#     return allWords

def extractContentFromPDF(pdfPath):
    pdfDocument = fitz.open(pdfPath)

    pages = []

    for pageNumber, page in enumerate(pdfDocument, start = 1):
        pageText = page.get_text("text").strip()

        if pageText:
            pages.append({
                "source": os.path.basename(pdfPath),
                "page": pageNumber,
                "text": pageText
            })

    pdfDocument.close()
    return pages