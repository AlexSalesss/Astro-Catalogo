# 🔭 AstroCatalog

Catálogo de objetos astronômicos para o terminal, escrito em Python. Permite listar, pesquisar, cadastrar e excluir objetos como estrelas, galáxias, nebulosas e exoplanetas, além de exportar resultados para arquivos JSON.

## Funcionalidades

- **Listar** todos os objetos do catálogo
- **Pesquisar** por nome, tipo ou constelação (sem diferenciar maiúsculas de minúsculas)
- **Cadastrar** novos objetos, com validação da distância
- **Excluir** objetos (protegido por senha de administrador, com limite de 5 tentativas)
- **Exportar** listagens e resultados de busca para JSON, sem sobrescrever exportações anteriores
- **Persistência** automática: cadastros e exclusões são salvos em `catalogo.json`

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa (usa apenas `json` e `os` da biblioteca padrão)

## Como executar

1. Coloque o script Python e o arquivo `catalogo.json` na mesma pasta.
2. No terminal, dentro dessa pasta, execute:

```bash
python astrocatalog.py
```

Se o `catalogo.json` não existir, o programa inicia com três objetos de exemplo (Sirius, Andromeda e Nebulosa de Orion) e cria o arquivo no primeiro cadastro ou exclusão.

## Menu principal

```
===== ASTROCATALOG =====
1 - Listar objetos
2 - Pesquisar objeto
3 - Cadastrar objeto
4 - Excluir objeto
0 - Sair
```

| Opção | O que faz |
|-------|-----------|
| 1 | Exibe todos os objetos e oferece exportar a lista para JSON |
| 2 | Abre o submenu de pesquisa (nome, tipo ou constelação) e oferece exportar os resultados |
| 3 | Pede nome, tipo, constelação e distância em anos-luz e salva no catálogo |
| 4 | Pede a senha de administrador, busca o objeto pelo nome e confirma antes de excluir |
| 0 | Encerra o programa |

## Formato dos dados

O catálogo é uma lista de objetos JSON no arquivo `catalogo.json`:

```json
{
    "nome": "Sirius",
    "tipo": "Estrela",
    "constelacao": "Cão Maior",
    "distancia_anos_luz": 8.6
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | texto | Nome do objeto |
| `tipo` | texto | Categoria do objeto (veja abaixo) |
| `constelacao` | texto | Constelação onde o objeto se encontra |
| `distancia_anos_luz` | número | Distância da Terra em anos-luz (não pode ser negativa) |

### Tipos presentes no catálogo

Estrela, Nebulosa, Galáxia, Aglomerado Estelar, Exoplaneta, Buraco Negro, Remanescente de Supernova, Pulsar e Quasar.

Ao cadastrar um objeto, o tipo é livre: você pode criar novas categorias.

## Exportação de resultados

Ao listar ou pesquisar, o programa pergunta se você deseja exportar o resultado. Os arquivos são nomeados automaticamente para que nenhum seja sobrescrito:

```
resultados.json
resultados(1).json
resultados(2).json
...
```

## Estrutura do projeto

```
.
├── astrocatalog.py     # Código do programa
├── catalogo.json       # Banco de dados do catálogo
├── resultados*.json    # Exportações geradas pelo programa (ignoradas pelo Git)
├── .gitignore
├── LICENSE
└── README.md
```

## Observações importantes

- **Acentos importam na busca.** A pesquisa ignora maiúsculas e minúsculas, mas não acentos: buscar "Orion" não encontra "Órion". Use a grafia exatamente como está no catálogo.
- **A busca é por correspondência exata.** Pesquisar "Nebulosa" por nome não retorna "Nebulosa de Orion"; é preciso digitar o nome completo.
- **Senha de administrador.** A senha está definida no próprio código (`SENHA_ADMIN`). Altere-a antes de compartilhar ou publicar o projeto.
- **Distâncias aproximadas.** Os valores do catálogo são aproximados e servem para fins educacionais.

## Ideias para o futuro

- Busca ignorando acentos e por correspondência parcial
- Edição de objetos já cadastrados
- Paginação ao listar catálogos grandes
- Ordenação por distância ou nome
- Senha fora do código (variável de ambiente ou hash)

## Licença

- MIT License
