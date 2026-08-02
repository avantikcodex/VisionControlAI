class ConversationState:

    def __init__(self):

        self.last_topic = None

        self.last_response = None

        self.active_mode = None

    def remember(self, topic, response):

        self.last_topic = topic

        self.last_response = response