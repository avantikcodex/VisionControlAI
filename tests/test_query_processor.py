from brain.knowledge.query_processor import QueryProcessor


processor = QueryProcessor()

while True:

    sentence = input("\nYou : ")

    result = processor.process(sentence)

    print(result)