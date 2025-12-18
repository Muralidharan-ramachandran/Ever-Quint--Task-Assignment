from agent_builder import build_agent

agent = build_agent()

def test_slot_logic():
    q = "A meeting needs 60 minutes. Slots: 09:00–09:30, 09:45–10:30, 11:00–12:00. Which fit?"
    r = agent.solve(q)
    assert r["status"] == "success"
