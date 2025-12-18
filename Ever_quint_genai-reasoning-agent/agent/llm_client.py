import openai

class LLMClient:
    def __init__(self, model="gpt-4.1-mini"):
        self.model = model

    def call(self, prompt):
        completion = openai.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
