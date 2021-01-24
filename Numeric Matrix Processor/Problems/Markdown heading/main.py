def heading(heading, level=1):
    level = 1 if level < 1 else 6 if level > 6 else level
    return ('#' * level) + ' ' + heading
