from brain.knowledge.answer_generator import AnswerGenerator

PASSED = 0
FAILED = 0


def check(name, function):
    global PASSED, FAILED

    print(f"\n[TEST] {name}")

    try:
        result = function()

        if result is False:
            FAILED += 1
            print(f"[FAIL] {name}")
        else:
            PASSED += 1
            print(f"[PASS] {name}")

    except Exception as error:
        FAILED += 1
        print(f"[FAIL] {name}")
        print(f"       {type(error).__name__}: {error}")


def test_core_imports():

    from brain.core.vexa_core import VexaCore
    from brain.core.pipeline import Pipeline
    from brain.core.request import Request
    from brain.core.response import Response
    from brain.decision.dispatcher import Dispatcher

    return True


def test_knowledge():

    from knowledge.knowledge_manager import KnowledgeManager

    km = KnowledgeManager()

    if km.app("chrome") is None:
        raise AssertionError("Chrome not found")

    if km.website("youtube") is None:
        raise AssertionError("YouTube not found")

    return True


def test_answer_generator():

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

    if not isinstance(answer, str):
        raise AssertionError("AnswerGenerator did not return text")

    if "Artificial Intelligence" not in answer:
        raise AssertionError("Expected answer content missing")

    if "Source" not in answer:
        raise AssertionError("Expected source information missing")

    return True


def test_learning_engine():

    from brain.learning.learning_engine import LearningEngine

    engine = LearningEngine()

    result = engine.learn(
        "Phase 1 verification question",
        "Phase 1 verification answer"
    )

    if result is not True:
        raise AssertionError("Learning engine failed")

    return True


def test_self_learning():

    from brain.learning.learning_engine import LearningEngine

    engine = LearningEngine()

    engine.feedback_response(
        "Phase 1 self learning test",
        True
    )

    return True


def test_automation_engine():

    from automation.automation_engine import AutomationEngine

    engine = AutomationEngine()

    if engine.app is None:
        raise AssertionError("App controller missing")

    if engine.browser is None:
        raise AssertionError("Browser controller missing")

    if engine.keyboard is None:
        raise AssertionError("Keyboard controller missing")

    if engine.mouse is None:
        raise AssertionError("Mouse controller missing")

    return True


def test_app_controller():

    from automation.app_controller import AppController

    controller = AppController()

    if controller is None:
        raise AssertionError("AppController failed")

    return True


def test_browser_controller():

    from automation.browser_controller import BrowserController

    controller = BrowserController()

    if controller is None:
        raise AssertionError("BrowserController failed")

    return True


def test_keyboard_controller():

    from automation.keyboard_controller import KeyboardController

    controller = KeyboardController()

    if controller is None:
        raise AssertionError("KeyboardController failed")

    return True


def test_mouse_controller():

    from automation.mouse_controller import MouseController

    controller = MouseController()

    if controller is None:
        raise AssertionError("MouseController failed")

    return True


def test_dispatcher():

    from brain.decision.dispatcher import Dispatcher

    dispatcher = Dispatcher()

    if dispatcher.automation is None:
        raise AssertionError("Dispatcher automation missing")

    return True


def test_vexa_core():

    from brain.core.vexa_core import VexaCore

    core = VexaCore()

    if core.pipeline is None:
        raise AssertionError("Pipeline missing")

    if core.dispatcher is None:
        raise AssertionError("Dispatcher missing")

    return True


def test_pipeline():

    from brain.core.pipeline import Pipeline
    from brain.core.request import Request

    pipeline = Pipeline()

    request = Request("open chrome")

    result = pipeline.process(request)

    if result is None:
        raise AssertionError("Pipeline returned None")

    if result.decision is None:
        raise AssertionError("Pipeline produced no decision")

    return True


def test_decision():

    from brain.core.pipeline import Pipeline
    from brain.core.request import Request

    pipeline = Pipeline()

    request = Request("open chrome")

    result = pipeline.process(request)

    decision = result.decision

    if decision is None:
        raise AssertionError("Decision missing")

    if not getattr(decision, "action", None):
        raise AssertionError("Decision action missing")

    if getattr(decision, "confidence", None) is None:
        raise AssertionError("Decision confidence missing")

    return True


def test_automation_error_handling():

    from automation.automation_engine import AutomationEngine

    engine = AutomationEngine()

    result = engine.execute("UNKNOWN_ACTION")

    if result is not False:
        raise AssertionError("Unknown action should return False")

    return True


def main():

    global PASSED, FAILED

    print("=" * 60)
    print("VEXA PHASE 1 MASTER TEST")
    print("=" * 60)

    check("Core imports", test_core_imports)
    check("Knowledge system", test_knowledge)
    check("Answer generator", test_answer_generator)
    check("Learning engine", test_learning_engine)
    check("Self learning", test_self_learning)
    check("Automation engine", test_automation_engine)
    check("Application controller", test_app_controller)
    check("Browser controller", test_browser_controller)
    check("Keyboard controller", test_keyboard_controller)
    check("Mouse controller", test_mouse_controller)
    check("Dispatcher", test_dispatcher)
    check("VEXA core", test_vexa_core)
    check("Pipeline processing", test_pipeline)
    check("Decision system", test_decision)
    check("Automation error handling", test_automation_error_handling)

    print("\n" + "=" * 60)
    print("PHASE 1 MASTER TEST RESULT")
    print("=" * 60)

    print(f"Tests Passed : {PASSED}")
    print(f"Tests Failed : {FAILED}")

    if FAILED == 0:
        print("\nPHASE 1 MASTER TEST : PASSED")
        print("PHASE 1 SOFTWARE SYSTEM : VERIFIED")
    else:
        print("\nPHASE 1 MASTER TEST : FAILED")
        print("PHASE 1 SOFTWARE SYSTEM : NOT VERIFIED")

    print("=" * 60)


if __name__ == "__main__":
    main()