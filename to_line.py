with open('problem/3.txt', 'r') as file:
    text = file.read()

single_line_text = "".join(text.split("\n"))
print(single_line_text)