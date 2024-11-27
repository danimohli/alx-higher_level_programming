def text_indentation(text):
    """
    Prints text with two newlines after each '.', '?', or ':'.
    No space should appear at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False

    for char in text:
        if char in ".?:":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            skip_space = False
        else:
            result += char
            skip_space = False

    print(result.strip())
