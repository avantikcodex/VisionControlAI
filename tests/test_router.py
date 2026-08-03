from brain.knowledge.query_processor import QueryProcessor
from brain.knowledge.topic_classifier import classify_topic
from brain.knowledge.knowledge_router import route

processor = QueryProcessor()

print("=" * 60)
print("KNOWLEDGE ROUTER TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    query = processor.process(sentence)

    topic = classify_topic(sentence)

    destination = route(query, topic)

    print("\nQuery :", query)

    print("Topic :", topic)

    print("Destination :", destination)