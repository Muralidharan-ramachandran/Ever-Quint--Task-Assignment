import json
from .llm_client import LLMClient

class Executor:
    def __init__(self, client: LLMClient, prompt):
        self.client = client
        self.prompt_template = prompt

    def execute(self, question, plan):
        p = self.prompt_template.replace("<question>", question).replace("<plan>", plan)
        response = self.client.call(p)
        return json.loads(response)
