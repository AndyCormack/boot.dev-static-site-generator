import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_eq(self):
        text = "This is a text node"
        node = TextNode("This is a text node")
        self.assertEqual(text, node.text)
        self.assertTrue(text in str(node))

    def test_text_not_eq(self):
        node = TextNode("This is a text node")
        node2 = TextNode("This is a different text node")
        self.assertNotEqual(node, node2)

    def test_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", url="https://www.google.com")
        node2 = TextNode("This is a text node", url="https://www.google.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", url="https://www.google.com")
        node2 = TextNode("This is a text node", url="https://www.bing.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(
            str(node), "TextNode(This is a text node, bold, https://www.google.com)"
        )

    def test_edge_url(self):
        node = TextNode("This is a text node", url=None)
        self.assertEqual(node.url, None)
        self.assertEqual(str(node), "TextNode(This is a text node, normal, None)")


if __name__ == "__main__":
    unittest.main()
