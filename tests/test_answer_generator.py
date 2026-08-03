from brain.knowledge.query_processor import QueryProcessor
from brain.knowledge.topic_classifier import classify_topic
from brain.knowledge.knowledge_router import route
from brain.knowledge.search_manager import search
from brain.knowledge.answer_generator import AnswerGenerator

processor = QueryProcessor()
generator = AnswerGenerator()

print("=" * 60)
print("ANSWER GENERATOR TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    query = processor.process(sentence)

    topic = classify_topic(sentence)

    destination = route(query, topic)

    result = search(destination, query)

    answer = generator.generate(query, result)

    print("\nVEXA\n")
    print(answer)