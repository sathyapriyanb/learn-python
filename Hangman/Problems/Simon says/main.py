def what_to_do(instructions):
    if any([instructions.startswith('Simon says'), instructions.endswith('Simon says')]):
        return 'I ' + instructions.replace('Simon says', '').strip()
    else:
        return "I won't do it!"
