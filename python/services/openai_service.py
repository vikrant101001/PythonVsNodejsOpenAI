import openai

class OpenAIService:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def analyze_dsa(self, prompt: str):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
