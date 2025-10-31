# md = """
# This is another paragraph with _italic_ text and `code` here


# - unorder list
# - another
# - other - bad
# """

# blocks = [block.strip(" ") for block in md.split("\n\n")]
# print(blocks)

# md = """
# > another quote
# badly formatted
# """

lst = ["", "line1", "line2", ""] 
string = "\n".join(lst)
print(string)
