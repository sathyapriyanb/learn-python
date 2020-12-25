raw_text = input()
mark_down_chars = list("*_~`")

for mark_down_char in mark_down_chars:
    raw_text = raw_text.lstrip(mark_down_char)
    raw_text = raw_text.rstrip(mark_down_char)

print(raw_text)
