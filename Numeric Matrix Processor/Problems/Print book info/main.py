def print_book_info(title, author=None, year=None):
    #  Write your code here
    print(
        f'"{title}"{" was written" if author or year else ""}{" by " + author if author else ""}{" in " + year if year else ""}')
