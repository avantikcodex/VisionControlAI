def test_answer_generator():

    from brain.knowledge.answer_generator import AnswerGenerator

    generator = AnswerGenerator()

    query = {
        "query_type": "EXPLAIN"
    }

    result = {
        "answer": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",
        "source": "Phase 1 Test"
    }

    answer = generator.generate(
        query,
        result
    )

    if answer is None:
        raise AssertionError(
            "AnswerGenerator returned None"
        )

    if not isinstance(answer, str):
        raise AssertionError(
            "AnswerGenerator did not return text"
        )

    if "Artificial Intelligence" not in answer:
        raise AssertionError(
            "Generated answer does not contain expected content"
        )

    if "Source" not in answer:
        raise AssertionError(
            "Generated answer does not contain source"
        )

    return True