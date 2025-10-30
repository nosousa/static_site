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


        # text = node.text
        # is_type = 0
        # if node.text.startswith(delimiter):
        #     is_type = 1
        #     text = text.lstrip(delimiter)
        
        # lst = text.split(delimiter, maxsplit=1)
        # while len(lst) > 1:
        #     if is_type:
        #         new_nodes.append(TextNode(lst[0], text_type))
        #     else:
        #         new_nodes.append(TextNode(lst[0], TextType.TEXT))
        #     is_type ^= 1
        #     lst = lst[1].split(delimiter, maxsplit=1)
        
        # if lst[0]:
        #     if is_type:
        #         raise Exception("invalid Markdown syntax: no closing delimiter")
        #     new_nodes.append(TextNode(lst[0], TextType.TEXT))
            
    # return new_nodes