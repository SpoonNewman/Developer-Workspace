def eat_ghost(power_pellet_active: bool, is_touching_ghost: bool):
    if power_pellet_active == True and is_touching_ghost == True:
        return True
    else:
        return False


def score(is_touching_pellet: bool, is_touching_dot: bool):
    if is_touching_pellet == True or is_touching_dot == True:
        return True
    else:
        return False

def lose(is_power_active: bool, is_touching_ghost: bool):
    if is_power_active != True and is_touching_ghost == True:
        return True
    else:
        return False


def win(has_eaten_all_dots: bool, is_power_active: bool, is_touching_ghost: bool):
    if has_eaten_all_dots == True and lose(is_power_active, is_touching_ghost) != True:
        return True
    else:
        return False



if __name__ == "__main__":
    # These are tests for the various cases
    assert eat_ghost(False, True) is False
    assert eat_ghost(True, False) is False
    assert eat_ghost(True, True) is True
    assert eat_ghost(False, False) is False

    assert score(True, False) is True
    assert score(False, True) is True
    assert score(True, True) is True
    assert score(False, False) is False

    assert lose(False, True) is True
    assert lose(True, False) is False
    assert lose(True, True) is False
    assert lose(False, False) is False

    assert win(True, True, True) is True
    assert win(False, True, True) is False
    assert win(False, False, True) is False
    assert win(False, False, False) is False
    assert win(True, False, False) is True
    assert win(True, True, False) is True
    assert win(True, False, True) is False

