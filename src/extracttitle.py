def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line[0:2] == "# ":
            title = line[2:]
            if title:
                return title
    raise Exception("no title header found")
