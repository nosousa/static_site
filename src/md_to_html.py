from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode
from utility_functions import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(inline_text):
    # convert inline text into a list of HTML nodes
    text_nodes = text_to_textnodes(inline_text)
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(markdown):
    html_root = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        lines = block.split("\n")

        match block_type:
            case BlockType.quote:
                quote = " ".join([line.lstrip(">").strip() for line in lines])
                block_node = ParentNode("blockquote", text_to_children(quote))

            case BlockType.unordered_list:
                block_node = ParentNode("ul", [])
                for line in lines:
                    line = line.lstrip("- ")
                    child_node = ParentNode("li", text_to_children(line))
                    block_node.children.append(child_node)
            
            case BlockType.ordered_list:
                block_node = ParentNode("ol", [])
                for i, line in enumerate(lines):
                    line = line.lstrip(f"{i + 1}. ")
                    child_node = ParentNode("li", text_to_children(line))
                    block_node.children.append(child_node)

            case BlockType.code:
                block = "\n".join(lines[1:-1])
                child_node = LeafNode("code", block)
                block_node = ParentNode("pre", [child_node])

            case BlockType.heading:
                count = len(block) - len(block.lstrip("#"))
                line = block[count + 1:].lstrip()
                if not line:
                    continue
                block_node = ParentNode(f"h{count}", text_to_children(line))
            
            case _:
                lines = [l.strip() for l in lines]
                block = " ".join([l for l in lines if l])
                block_node = ParentNode("p", text_to_children(block))
        
        html_root.children.append(block_node)

    return html_root