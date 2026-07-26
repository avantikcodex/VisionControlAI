MEMORY = []


def remember(command):

    MEMORY.append(command)


def recent():

    return MEMORY[-10:]