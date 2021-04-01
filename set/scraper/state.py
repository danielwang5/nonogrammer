from enum import IntEnum

class State(IntEnum):
    LOGIN = 0
    LOBBY = 1
    WAITING = 2
    GAME = 3
    OVER = 4

def get_state(source):
    if is_login(source):
        return State.LOGIN
    if is_lobby(source):
        return State.LOBBY
    if is_waiting(source):
        return State.WAITING
    if is_game(source):
        return State.GAME
    if is_over(source):
        return State.OVER
    raise Exception('Unknown state')

def is_login(source):
    # TODO
    pass

def is_lobby(source):
    # TODO
    pass

def is_waiting(source):
    # TODO
    pass

def is_game(source):
    # TODO
    pass

def is_over(source):
    # TODO
    pass