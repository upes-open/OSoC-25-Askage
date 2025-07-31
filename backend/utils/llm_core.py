import openai
import json


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
    
    def prompt_suggestions(self, webpage_content: str) -> list[str]:
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": f"You are Askage, a chrome extension what lets users ask questions about the webpage they are on. Based on the webpage user is currently on, generate 3 highly relevent prompt suggestions. You must respond in a JSON array with only 3 elements (string), with no markdown. Each suggestion must be around 5-6 words.\n\nHere's the example response JSON format: [\"<suggestion1>\", \"<suggestion2>\", ...]\n\nBelow is the webpage content:\n{webpage_content}"
            }]
        )
        
        reply = response.choices[0].message.content
        
        try:
            suggestions: list[str] = json.loads(reply)
            
            if not isinstance(suggestions, list) or len(suggestions) != 3:
                return ["Summarize this webpage"]

            return suggestions
        
        except Exception:
            return ["Summarize this webpage"]
