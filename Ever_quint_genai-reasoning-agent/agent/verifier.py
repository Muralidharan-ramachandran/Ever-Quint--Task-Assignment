import json
from .llm_client import LLMClient

class Verifier:
    def __init__(self, client: LLMClient, prompt):
        self.client = client
        self.prompt_template = prompt

    def verify(self, question, intermediate, answer):
        p = (self.prompt_template
             .replace("<q>", question)
             .replace("<text>", intermediate)
             .replace("<ans>", answer))
        response = self.client.call(p)
        return json.loads(response)
