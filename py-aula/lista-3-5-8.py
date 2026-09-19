# # EXERCÍCIO 3 --->
# produto = {"Nome": "Teclado", "preco": 120.0}

# try:
#   print(produto["estoque"])

# except KeyError:
#   print(f"Ocorreu um erro.")


# # EXERCÍCIO 4 --->          
# nome = "Marina"

# try:
#     nome.append("Silva")

# except AttributeError:
#     print(f"Tipo de erro: {type(nome).__name__}")


# # EXERCÍCIO 8 --->          
aluno_ok = {
    "nome": "Lia",
    "notas": {"Python": 8.5, "Calculo": 7.0}  
}

def exibir_nota(aluno, disciplina):
    try:
        nota = aluno["notas"][disciplina]
        print(f"Nota em {disciplina}: {nota}")
    except KeyError:
        print("Erro: A chave de 'notas' ou 'disciplina' não existe.")
    except TypeError:
        print("Erro: O objeto em 'aluno' não existe")

exibir_nota(aluno_ok, 'Python')
exibir_nota(aluno_ok, 'nome')
exibir_nota(None, 'python')