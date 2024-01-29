import os

def cadastrar(contatos):
  nome = input("Digite o nome do novo contato: \n ")
  telefone = input("Digite o telefone do novo contato: \n ")
  email = input("Digite o email do novo contato: \n ")
  contatos.append({"nome": nome, "telefone": telefone, "email": email, "is_favotite": False})
  back = input("Contato registrado com sucesso. Pressione enter para voltar")
  return contatos

def visualizar(contatos):
  for i in range(len(contatos)):
    for chave, valor in contatos[i].items():
      if chave == "is_favotite":
        valor = "✓" if valor == True else "✘"
      print(chave, "=", valor)
    print()
  back = input("Pressione enter para voltar")
  return

def editar(contatos):
  for i in range(len(contatos)):  
    itens = list(contatos[i].items())
    print(i+1, " ",itens[0][0], "=", itens[0][1], " ",itens[1][0], "=", itens[1][1])

  editar = input("Digite o ID do contato que voce quer editar: \n ")
  editar = int(editar) - 1
  if editar >= 0 and editar < len(contatos):
    o_que_editar = input("Digite o que deseja editar: \n 1 - Nome \n 2 - Telefone \n 3 - Email \n ")
    if o_que_editar == "1":
      nome = input("Digite o novo nome do contato: \n ")
      contatos[editar]["nome"] = nome
    elif o_que_editar == "2":
      telefone = input("Digite o novo telefone do contato: \n ")
      contatos[editar]["telefone"] = telefone
    elif o_que_editar == "3":
      email = input("Digite o novo email do contato: \n ")
      contatos[editar]["email"] = email
    back = input("O contato foi editado.Pressione enter para voltar")
  else:
    back = input("ID não encontrado.")
  return contatos

def favorito(contatos):
  for i in range(len(contatos)):
    itens = list(contatos[i].items())
    fav = "✓" if itens[3][1] == True else "✘"
    print(i+1, " ",itens[0][1], " - ", itens[1][1], " - ", fav)

  favoritar = input("Digite o ID do contato que voce quer favoritar/desfavoritar: \n ")
  favoritar = int(favoritar) - 1
  if favoritar >= 0 and favoritar < len(contatos):
    contatos[favoritar]["is_favotite"] = not contatos[favoritar]["is_favotite"]
    back = input("O contato foi favoritado/desfavoritado. Pressione enter para voltar")
  else:
    back = input("ID não encontrado.")
  return contatos

def lista_favoritos(contatos):
  for i in range(len(contatos)):
    if contatos[i]["is_favotite"] == True:
      print(contatos[i]["nome"])
  back = input("Pressione enter para voltar")    
  return

def apagar(contatos):
  for i in range(len(contatos)):
    itens = list(contatos[i].items())
    print(i+1, " ",itens[0][1], " - ", itens[1][1], " - ", itens[3][1])

  apagar = input("Digite o ID do contato que voce quer apagar: \n ")
  apagar = int(apagar) - 1
  if apagar >= 0 and apagar < len(contatos):
    contatos.pop(apagar)
    back = input("O contato foi apagado. Pressione enter para voltar") 
  else:
    back = input("ID não encontrado.")
  return contatos

contatos = []

continuar = True
while continuar == True:
  # Limpa a tela
  os.system('cls')
  # - Escolha opção
  opcao = input("Digite 1 para cadastrar um contato, \n" +
                "2 para visualizar a lista de contatos, \n" +
                "3 para editar um contato, \n" +
                "4 para marcar/desmarcar um contato como favorito, \n" +
                "5 para ver uma lista de contatos favoritos, \n" +
                "6 para apagar um contato, \n" +
                "7 para sair: ")
  
  os.system('cls')
  # - Cadastrar um novo contato
  if opcao == "1":
    cadastrar(contatos)

  # - Visualizar a lista de contatos cadastrados
  elif opcao == "2":
    visualizar(contatos)
    
  # - Editar um contato
  elif opcao == "3":
    editar(contatos)

  # - Marcar/desmarcar um contato como favorito
  elif opcao == "4":
    favorito(contatos)
  
  # - Ver uma lista de contatos favoritos
  elif opcao == "5":
    lista_favoritos(contatos)
  
  # - Apagar um contato
  elif opcao == "6":
    apagar(contatos)

  else:
    quit()