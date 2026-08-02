from brain.decision.decision import Decision

decision = Decision(
    action="OPEN_APPLICATION",
    target="Google Chrome",
    confidence=98,
    need_confirmation=False,
    risk="LOW"
)

print(decision)