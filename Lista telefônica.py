ListaTelefônica = {}

print("1. Mostra Lista Telefonica")
print("2. Acrescentar Entrada (Nome, Número)")
print("3. Retirar Entrada (Nome)")
print("4. Procurar Número")
print("5. Mostra todos os nomes dos contatos")
print("6. Atualizar contato")
print("7. Terminar \n")

opções = 0


while opções != 7:
    try: opções = int(input("Insira a opção que deseja realizar: "))
    except ValueError:
        print("Valor inválido \n")
    else:
        if opções > 7 or opções<1:
            print("Valor inválido, só são aceitos opções de 1 a 7 \n")
        else:
            print('\n')
            if opções == 1:
                print("A lista telefônica é: \n ")
                for key, value in ListaTelefônica.items():
                    print(key,': ', value)
                print("\n")        
            
            elif opções == 2:
                print("Acrescente um contato na lista telefônica \n ")
                Nome = input("Insira o nome: ")
                Telefone = int(input("Insira o número de telefone: "))
                ListaTelefônica[Nome] = Telefone
                print("Contato adicionado \n")
                
            elif opções == 3:
                print("Remova um contato na lista telefônica \n ")
                Nome = input("Insira o nome do contato que deseja remover: ")
                if Nome in ListaTelefônica:
                    del ListaTelefônica[Nome]
                    print("Contato excluído \n")
                else:
                    print("O contato não está na lista \n")
                
            elif opções == 4:
                print("Encontre um contato na lista telefônica \n ")
                Nome = input("Insira o nome do contato que deseja encontrar: ")
                if Nome in ListaTelefônica:
                    print("O número é: ", ListaTelefônica[Nome], "\n")
                else:
                    print("O contato não está na lista \n")
                
            elif opções == 5:
                print("Os nomes da lista telefônica são \n ")
                for key in ListaTelefônica.keys():
                    print(key)
                print("\n")
                    
            elif opções == 6:
                print("Atualize um contato na lista telefônica \n ")
                Nome = input("Insira o nome do contato que deseja atualizar: ")
                Telefone = int(input("Insira o número novo: "))
                ListaTelefônica[Nome] = Telefone
                print("Valor atualizado \n")

print("Operação finalizada!!")