from brain.confidence.confidence_engine import ConfidenceEngine

engine = ConfidenceEngine()

print("=" * 60)
print("CONFIDENCE ENGINE TEST")
print("=" * 60)

result = engine.evaluate(

    decision="OPEN_APPLICATION",

    knowledge_found=True

)

print(result)

print()

result = engine.evaluate(

    decision="SEARCH",

    knowledge_found=False

)

print(result)

print()

result = engine.evaluate(

    decision=None,

    knowledge_found=False

)

print(result)