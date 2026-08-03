WAKE_WORDS = [

    "vexa",

    "hey vexa",

    "hello vexa"

]


def detected(sentence):

    sentence = sentence.lower()

    for word in WAKE_WORDS:

        if word in sentence:

            return True

    return False