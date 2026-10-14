import json
import os

ARQUIVO_CATALOGO = "catalogo.json"


def carregar_catalogo():
    if os.path.exists(ARQUIVO_CATALOGO):
        with open(ARQUIVO_CATALOGO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return [
        {
            "nome": "Sirius",
            "tipo": "Estrela",
            "constelacao": "Cão Maior",
            "distancia_anos_luz": 8.6
        },
        {
            "nome": "Andromeda",
            "tipo": "Galáxia",
            "constelacao": "Andromeda",
            "distancia_anos_luz": 2537000
        },
        {
            "nome": "Nebulosa de Orion",
            "tipo": "Nebulosa",
            "constelacao": "Orion",
            "distancia_anos_luz": 1350
        }
    ] # base inicial de dados caso não exista o arquivo com o catalago


def salvar_catalogo(catalogo):
    with open(ARQUIVO_CATALOGO, "w", encoding="utf-8") as arquivo:
        json.dump(catalogo, arquivo, ensure_ascii=False, indent=4)


catalogo = carregar_catalogo()

print(f"Catálogo carregado: {len(catalogo)} objetos.")

def exibeObjeto(objeto):
      print(f"\nNome: {objeto['nome']}")
      print(f"Tipo: {objeto['tipo']}")
      print(f"Constelação: {objeto['constelacao']}")
      print(f"Distância: {objeto['distancia_anos_luz']} anos-luz\n")

def lista_catalogo():
    if not catalogo:
        return

    print(f"\n===== CATÁLOGO ({len(catalogo)} objetos encontrados) =====")
    for objeto in catalogo:
        exibeObjeto(objeto)

    exportar_json(catalogo)

def buscar_objetos(campo, valor):
    valor = valor.strip().casefold()
    encontrados = []

    for objeto in catalogo:
        if objeto[campo].strip().casefold() == valor:
            encontrados.append(objeto)

    if encontrados:
        print(f"\nEncontrados: {len(encontrados)} objeto(s)")
        for objeto in encontrados:
            exibeObjeto(objeto)
    else:
        print("\nNenhum objeto encontrado.")
    
    return encontrados

def Buscar_Por_Nome():
    Nome = input("\nDigite o nome do Objeto: ").strip().casefold()
    resultados = buscar_objetos("nome", Nome)
    exportar_json(resultados)

def Buscar_Por_Tipo():
    Busca_Tipo = input("\nDigite o tipo de Objeto: ").strip().casefold()
    resultados = buscar_objetos("tipo", Busca_Tipo)
    exportar_json(resultados)

def Buscar_Por_Constelacao():
    Constelacao = input("\nDigite o nome da Constelação do Objeto: ").strip().casefold()
    resultados = buscar_objetos("constelacao", Constelacao)
    exportar_json(resultados)

def Cadastrar_Novo_Objeto():
  novo_objeto = {}
  novo_objeto["nome"] = input("Digite o nome do objeto: ").strip().title()
  novo_objeto["tipo"] = input("Digite o tipo do objeto: ").strip().title()
  novo_objeto["constelacao"] = input("Digite a constelação do objeto: ").strip().title()

  while True:
    distancia = input("Distância em anos-luz: ").strip()

    try:
        distancia = float(distancia.replace(",", "."))

        if distancia < 0:
            print("A distância não pode ser negativa.")
            continue

        break

    except ValueError:
        print("Digite uma distância numérica válida.")

  novo_objeto["distancia_anos_luz"] = distancia
  catalogo.append(novo_objeto)
  salvar_catalogo(catalogo)
  print("\nObjeto cadastrado com sucesso!")

def proximo_nome_arquivo(base="resultados", extensao=".json"):
    if not os.path.exists(f"{base}{extensao}"):
        return f"{base}{extensao}"

    numero = 1
    while os.path.exists(f"{base}({numero}){extensao}"):
        numero += 1

    return f"{base}({numero}){extensao}"

def  exportar_json(resultados):
    if not resultados:
        return
    while True:
            opcao = input(
                "Deseja exportar os resultados para um arquivo JSON? (S/N): "
            ).strip().upper()

            if opcao == "S" or opcao == "SIM":
                nome_arquivo = proximo_nome_arquivo()
                with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                    json.dump(resultados, arquivo, ensure_ascii=False, indent=4)

                print(f"Resultados exportados para {nome_arquivo}")
                break

            elif opcao == "N" or opcao == "NÃO" or opcao == "NAO":
                print("Operação cancelada.")
                break

            else:
                print("Resposta inválida. Digite S ou N.")

SENHA_ADMIN = "Astro135"

def autenticar_admin():
    tentativas = 0

    while tentativas < 5:
        senha = input("Digite a senha de administrador: ")

        if senha == SENHA_ADMIN:
            print("Acesso autorizado!")
            return True
        else:
            tentativas += 1
            restantes = 5 - tentativas
            print(f"\nSenha incorreta. Tentativas restantes: {restantes}\n")

    print("Limite de tentativas atingido. Acesso negado.")
    return False

def excluir_dados():
    if not autenticar_admin():
        return
    objeto = input("Digite o nome do objeto a ser excluído: ").strip()
    encontrados = buscar_objetos("nome", objeto)

    if not encontrados:
        print("Nenhum objeto encontrado para exclusão.")
        return
    while True:
        opcao = input(
            "Deseja realmente excluir os objetos encontrados? (S/N): "
        ).strip().upper()
        if opcao == "S" or opcao == "SIM":
            for objeto in encontrados:
                catalogo.remove(objeto)
            salvar_catalogo(catalogo)
            print("Objetos excluídos com sucesso!")
            break
        elif opcao == "N" or opcao == "NÃO" or opcao == "NAO":
            print("Operação cancelada.")
            break

        else:
            print("Resposta inválida. Digite S ou N.")

while True:
    print("\n===== ASTROCATALOG =====")
    print("1 - Listar objetos")
    print("2 - Pesquisar objeto")
    print("3 - Cadastrar objeto")
    print("4 - Excluir objeto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("Você escolheu listar objetos!")
        lista_catalogo()

    elif opcao == "2":
        print("Você escolheu pesquisar um objeto!")
        while True:
          print("\n===== ASTROCATALOG (Pesquisar objeto) =====")
          print("1 - Pesquisar por nome")
          print("2 - Pesquisar por tipo")
          print("3 - Pesquisar por constelação")
          print("0 - Sair")

          opcao01 = input("Escolha uma opção: ").strip()
          if opcao01 == "1":
            Buscar_Por_Nome()
            break
          elif opcao01 == "2":
            Buscar_Por_Tipo()
            break
          elif opcao01 == "3":
            Buscar_Por_Constelacao()
            break
          elif opcao01 == "0":
            print("Encerrando o AstroCatalog (Pesquisar Objeto). Até mais!")
            break


          else:
            print("Opção inválida. Tente novamente.")

    elif opcao == "3":
        print("Você escolheu cadastrar um objeto!")
        Cadastrar_Novo_Objeto()


    elif opcao == "0":
        print("\nEncerrando o AstroCatalog. Até mais!")
        break

    elif opcao == "4":
        print("Você escolheu excluir um objeto! (Somente Adm)")
        excluir_dados()

    else:
        print("Opção inválida. Tente novamente.")
