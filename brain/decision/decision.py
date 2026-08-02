class Decision:

    def __init__(
        self,
        action=None,
        target=None,
        confidence=0,
        need_confirmation=False,
        risk="LOW"
    ):

        self.action = action
        self.target = target
        self.confidence = confidence
        self.need_confirmation = need_confirmation
        self.risk = risk

    def __repr__(self):

        return (
            f"Decision("
            f"action={self.action}, "
            f"target={self.target}, "
            f"confidence={self.confidence}, "
            f"need_confirmation={self.need_confirmation}, "
            f"risk={self.risk})"
        )