from agent_builder import build_agent

agent = build_agent()

def test_time_diff():
    q = "If a train leaves at 14:30 and arrives at 18:05, how long is the trip?"
    r = agent.solve(q)
    assert r["status"] == "success"
