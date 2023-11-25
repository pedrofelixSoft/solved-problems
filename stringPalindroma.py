string = input("Escreva a Palavra: ")
if string == string[::-1]:
    print("É uma Palavra Palindroma!")
    exit()
print("Não é uma palavra Palindroma! ")
