from brain.knowledge.query_processor import QueryProcessor
from brain.knowledge.topic_classifier import classify_topic
from brain.knowledge.knowledge_router import route
from brain.knowledge.search_manager import search
from brain.knowledge.answer_generator import AnswerGenerator


class KnowledgeEngine:

    def __init__(self):

        self.processor = QueryProcessor()
        self.generator = AnswerGenerator()

    def process(self, sentence):

        # Step 1: Process query
        query = self.processor.process(sentence)

        # Step 2: Classify topic
        topic = classify_topic(sentence)

        # Step 3: Route
        destination = route(query, topic)

        # Step 4: Search
        result = search(destination, query)

        # Step 5: Generate answer
        answer = self.generator.generate(query, result)

        return {
            "query": query,
            "topic": topic,
            "destination": destination,
            "result": result,
            "answer": answer
        }