import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

class TestBlockSplit(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_markdown_to_blocks_newlines(self):
            md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_block_to_type(self):
            md = """
# This is bolded heading




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items


## This is a sub heading

1. This is an
2. ordered
3. list.

> quote in several lines
> of text

```
Markdown code comes here
```

"""
            blocks = markdown_to_blocks(md)
            types = [block_to_block_type(block) for block in blocks]
            expected = [BlockType.heading, 
                        BlockType.paragraph, 
                        BlockType.unordered_list, 
                        BlockType.heading,
                        BlockType.ordered_list,
                        BlockType.quote,
                        BlockType.code]
            self.assertListEqual(types, expected)


if __name__ == "__main__":
    unittest.main()