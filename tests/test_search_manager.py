from brain.knowledge.query_processor import QueryProcessor
from brain.knowledge.topic_classifier import classify_topic
from brain.knowledge.knowledge_router import route
from brain.knowledge.search_manager import search

processor = QueryProcessor()

print("=" * 60)
print("SEARCH MANAGER TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    query = processor.process(sentence)

    topic = classify_topic(sentence)

    destination = route(query, topic)

    result = search(destination, query)

    print("\nDestination :", destination)

    print("Source :", result["source"])

    print("Answer :", result["answer"])