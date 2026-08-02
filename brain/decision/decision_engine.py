from brain.decision.decision import Decision


class DecisionEngine:

    def make_decision(self, intent, entity):

        if entity is None:

            return Decision(

                action="UNKNOWN",

                target=None,

                confidence=0,

                need_confirmation=False,

                risk="LOW"

            )

        entity_type = entity["type"]

        entity_value = entity["value"]

        # ---------- APPLICATION ----------

        if entity_type == "APPLICATION":

            return Decision(

                action="OPEN_APPLICATION",

                target=entity_value,

                confidence=98,

                need_confirmation=False,

                risk="LOW"

            )

        # ---------- WEBSITE ----------

        if entity_type == "WEBSITE":

            return Decision(

                action="OPEN_WEBSITE",

                target=entity_value,

                confidence=98,

                need_confirmation=False,

                risk="LOW"

            )

        return Decision(

            action="UNKNOWN",

            target=None,

            confidence=0,

            need_confirmation=False,

            risk="LOW"

        )