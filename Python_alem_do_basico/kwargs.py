# Númro variável de argumentos de palavras-chave
def print_info(**person):
    print(person)


print_info()
print_info(name='Steve')
print_info(name='steve', age=22)
