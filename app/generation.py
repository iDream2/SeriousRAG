from openai import OpenAI
from dotenv import load_dotenv
import os
def generateAnswers(question,context):
    load_dotenv()
    client = OpenAI(api_key = os.getenv("OPEN_AI_KEY")) 
    prompt = f"""Answer the following question with the context provided below:  
    
        question : {question}

        context : {context}
    If you do not have sufficient information, say that you don't have sufficient context
    """
    response = client.responses.create(
        model = "gpt-4o-mini",
        input =prompt
    )

    answer = response.output_text
    return answer