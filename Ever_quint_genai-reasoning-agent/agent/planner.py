from .llm_client import LLMClient

class Planner:
    def __init__(self, client: LLMClient, prompt):
        self.client = client
        self.prompt_template = prompt

    def plan(self, question):
        prompt = self.prompt_template.replace("{{QUESTION}}", question)
        response = self.client.call(prompt)
        return response
