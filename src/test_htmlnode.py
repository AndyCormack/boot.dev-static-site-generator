import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.google.com"}
        )
        node2 = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.google.com"}
        )
        self.assertEqual(node, node2)

    def test_tag_eq(self):
        node = HTMLNode("div")
        node2 = HTMLNode("div")
        self.assertEqual(node, node2)

    def test_tag_not_eq(self):
        node = HTMLNode("div")
        node2 = HTMLNode("span")
        self.assertNotEqual(node, node2)

    def test_value_eq(self):
        node = HTMLNode("div", "This is a text node")
        node2 = HTMLNode("div", "This is a text node")
        self.assertEqual(node, node2)

    def test_value_not_eq(self):
        node = HTMLNode("div", "This is a text node")
        node2 = HTMLNode("div", "This is a different text node")
        self.assertNotEqual(node, node2)

    def test_children_eq(self):
        node = HTMLNode("div", "This is a text node", [])
        node2 = HTMLNode("div", "This is a text node", [])
        self.assertEqual(node, node2)

    def test_children_not_eq(self):
        node = HTMLNode("div", "This is a text node", [])
        node2 = HTMLNode(
            "div", "This is a text node", ["This is a different text node"]
        )
        self.assertNotEqual(node, node2)

    def test_props_eq(self):
        node = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.google.com"}
        )
        node2 = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.google.com"}
        )
        self.assertEqual(node, node2)

    def test_props_not_eq(self):
        node = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.google.com"}
        )
        node2 = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.bing.com"}
        )
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(
            "div", "This is a text node", [], {"href": "https://www.google.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_two_props_to_html(self):
        node = HTMLNode(
            "div",
            "This is a text node",
            [],
            {"href": "https://www.google.com", "class": "test classes"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" class="test classes"'
        )
