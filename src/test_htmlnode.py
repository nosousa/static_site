import unittest

from htmlnode import HTLMNode


class TestTextNode(unittest.TestCase):
    PROPS = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    def test_1(self):
        node = HTLMNode("p", "text inside paragraph", [], self.PROPS)
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_2(self):
        child_node = HTLMNode(None, "text inside paragraph",)
        parent_node = HTLMNode("p", None, [child_node], self.PROPS)
        print(parent_node)
        self.assertTrue(True)
    
    def test_3(self):
        node = HTLMNode("p", None, None, self.PROPS)
        print(node.props_to_html())
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()