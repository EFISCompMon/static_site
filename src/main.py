from textnode import TextType, TextNode

def main():
    TestNode = TextNode("Anchor Text", TextType.LINK, "https://www.boot.dev")
    print(TestNode)

main()