CURRENT_CONTEXT = {}


def set_context(key, value):

    CURRENT_CONTEXT[key] = value


def get_context(key):

    return CURRENT_CONTEXT.get(key)