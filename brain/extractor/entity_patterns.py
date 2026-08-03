import re

PROFILE_PATTERNS = {
    "name": [
        re.compile(r"my name is (.+)", re.IGNORECASE),
        re.compile(r"i am (.+)", re.IGNORECASE),
    ],

    "college": [
        re.compile(r"i study at (.+)", re.IGNORECASE),
        re.compile(r"my college is (.+)", re.IGNORECASE),
    ],

    "city": [
        re.compile(r"i live in (.+)", re.IGNORECASE),
        re.compile(r"i am from (.+)", re.IGNORECASE),
    ]
}


PREFERENCE_PATTERNS = {
    "favorite_language": [
        re.compile(r"i like (.+)", re.IGNORECASE),
        re.compile(r"i love (.+)", re.IGNORECASE),
        re.compile(r"my favorite language is (.+)", re.IGNORECASE),
    ],

    "favorite_browser": [
        re.compile(r"my favorite browser is (.+)", re.IGNORECASE),
    ],

    "favorite_ide": [
        re.compile(r"my favorite ide is (.+)", re.IGNORECASE),
    ]
}


GOAL_PATTERNS = {
    "goal": [
        re.compile(r"i want to become (.+)", re.IGNORECASE),
        re.compile(r"my goal is (.+)", re.IGNORECASE),
        re.compile(r"my dream is (.+)", re.IGNORECASE),
    ]
}