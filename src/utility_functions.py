import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        splitted = node.text.split(delimiter)
        if len(splitted) % 2 == 0:
            raise ValueError("invalid Markdown syntax: no closing delimiter")
        
        for i, text in enumerate(splitted):
            if not text:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        matches = extract_markdown_images(node.text)
        text = node.text
        for img_alt, img_url in matches:
            prev, text = text.split(f"![{img_alt}]({img_url})", maxsplit=1)
            
            if prev:
                new_nodes.append(TextNode(prev, TextType.TEXT))
            
            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_url))
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        matches = extract_markdown_links(node.text)
        text = node.text
        for link_alt, link_url in matches:
            prev, text = text.split(f"[{link_alt}]({link_url})", maxsplit=1)
            
            if prev:
                new_nodes.append(TextNode(prev, TextType.TEXT))
            
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    it = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE)
    ]
    
    nodes = [TextNode(text, TextType.TEXT)]

    for delimeter, text_type in it:
        nodes = split_nodes_delimiter(nodes, delimeter, text_type)
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
