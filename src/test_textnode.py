import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_3(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a textier node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_4(self):
        node = TextNode("This is a alt text", TextType.IMAGE, None)
        node2 = TextNode("This is a alt text", TextType.IMAGE)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()