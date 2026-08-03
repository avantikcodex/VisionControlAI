from brain.knowledge.topic_classifier import classify_topic

print("=" * 50)
print("TOPIC CLASSIFIER TEST")
print("=" * 50)

while True:

    sentence = input("\nYou : ")

    topic = classify_topic(sentence)

    print("\nTopic :", topic)