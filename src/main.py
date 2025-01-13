from textnode import TextNode, TextType

print("hello world")


def main():
    text_node = TextNode("This is a text node", TextType.Bold, "https://www.google.com")
    print(text_node)


if __name__ == "__main__":
    main()
