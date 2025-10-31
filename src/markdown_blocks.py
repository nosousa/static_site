from enum import Enum

class BlockType(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote = 4
    unordered_list = 5
    ordered_list = 6

def markdown_to_blocks(markdown):
    blocks = [block.strip("\n ") for block in markdown.split("\n\n")]
    return [block for block in blocks if block]

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.heading
    elif block.startswith("```\n") and block.endswith("\n```"):
        return BlockType.code
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.quote
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.unordered_list
    elif all(line.startswith(f"{i + 1}. ") for i, line in enumerate(block.split("\n"))):
        return BlockType.ordered_list
    else:
        return BlockType.paragraph