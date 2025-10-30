import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=p, value=What a strange world, children=None, props={'class': 'primary'})",
        )

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

        node = LeafNode(None, "raw text")
        self.assertEqual(node.to_html(), "raw text")

    def test_leaf_errors(self):
        with self.assertRaises(TypeError):
            LeafNode("a")

        with self.assertRaises(ValueError):
            LeafNode("a", None).to_html()

    def test_isinstance(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertIsInstance(node.props, dict)

if __name__ == "__main__":
    unittest.main()