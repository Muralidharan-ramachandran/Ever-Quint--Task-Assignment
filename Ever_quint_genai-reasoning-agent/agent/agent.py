class ReasoningAgent:
    def __init__(self, planner, executor, verifier, max_retries=2):
        self.planner = planner
        self.executor = executor
        self.verifier = verifier
        self.max_retries = max_retries

    def solve(self, question):
        retries = 0
        all_checks = []

        while retries <= self.max_retries:
            plan = self.planner.plan(question)

            execution = self.executor.execute(question, plan)
            intermediate = execution["intermediate"]
            final_answer = execution["proposed_answer"]

            check = self.verifier.verify(question, intermediate, final_answer)
            all_checks.append(check)

            if check["passed"]:
                return {
                    "answer": final_answer,
                    "status": "success",
                    "reasoning_visible_to_user": "Solved using step-by-step reasoning.",
                    "metadata": {
                        "plan": plan,
                        "checks": all_checks,
                        "retries": retries
                    }
                }

            retries += 1

        return {
            "answer": None,
            "status": "failed",
            "reasoning_visible_to_user": "Verification failed.",
            "metadata": {
                "plan": plan,
                "checks": all_checks,
                "retries": retries
            }
        }
