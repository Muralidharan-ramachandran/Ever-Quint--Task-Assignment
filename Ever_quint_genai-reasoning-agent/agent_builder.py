from agent.llm_client import LLMClient
from agent.planner import Planner
from agent.executor import Executor
from agent.verifier import Verifier
from agent.agent import ReasoningAgent

def load_file(path):
    with open(path) as f:
        return f.read()

def build_agent():
    client = LLMClient()

    planner = Planner(client, load_file("agent/prompts/planner_prompt.txt"))
    executor = Executor(client, load_file("agent/prompts/executor_prompt.txt"))
    verifier = Verifier(client, load_file("agent/prompts/verifier_prompt.txt"))

    return ReasoningAgent(planner, executor, verifier)

if __name__ == "__main__":
    agent = build_agent()
    while True:
        q = input("\nQuestion: ")
        result = agent.solve(q)
        print(result)
