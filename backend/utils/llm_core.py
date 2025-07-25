import openai

class LLMCore:
    """
    Handles core LLM operations.
    """
    
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    def prompt(self, chat: list) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=chat
        )
        
        reply = response.choices[0].message
        return reply.content
