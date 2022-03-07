from nbformat import write


with open ("example.py") as content:
    print(content.read())



with open ("myfile.text","w") as content:
    content.write("Here is some Text\n This should be in next line")
    content.write