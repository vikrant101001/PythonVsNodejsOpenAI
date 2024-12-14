import openai
from fastapi import FastAPI
from pydantic import BaseModel

# Set your OpenAI API key and model directly here
OPENAI_API_KEY = "your_openai_api_key_here"
DEFAULT_MODEL = "gpt-3.5-turbo"  # You can replace with your preferred model

# Initialize OpenAI API client
openai.api_key = OPENAI_API_KEY

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for the request body
class QuestionRequest(BaseModel):
    question: str


@app.post("/analyze_dsa/")
async def analyze_dsa(question_request: QuestionRequest):
    question = question_request.question
    
    # Example base prompt (you can modify it as needed)
    base_prompt = """
    You are a DSA expert. Given a question related to Data Structures and Algorithms (DSA),
    identify the topics being asked and provide an explanation for it. Respond in a structured
    format with a list of topics and an explanation.
    """

    full_prompt = f"{base_prompt}\n\nQuestion: {question}"

    # Call OpenAI API for analysis
    response = openai.ChatCompletion.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": full_prompt}]
    )

    # Extract content from the response
    content = response.choices[0].message['content']

    # Return the structured response
    return {"question": question, "analysis": content}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
