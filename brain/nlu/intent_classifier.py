APPLICATION_WORDS = {

    "open",
    "launch",
    "start",
    "run"

}

BROWSER_WORDS = {

    "browse",
    "search",
    "google",
    "internet",
    "website"

}

MEDIA_WORDS = {

    "watch",
    "play",
    "listen",
    "music",
    "video",
    "videos"

}

SYSTEM_WORDS = {

    "shutdown",
    "restart",
    "sleep",
    "lock",
    "logout"

}


def classify_intent(tokens):

    for word in tokens:

        if word in APPLICATION_WORDS:

            return "APPLICATION"

        if word in BROWSER_WORDS:

            return "BROWSER"

        if word in MEDIA_WORDS:

            return "MEDIA"

        if word in SYSTEM_WORDS:

            return "SYSTEM"

    return "UNKNOWN"