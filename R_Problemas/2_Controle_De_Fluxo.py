# 1° Solicite ao usuário que informe seu tipo de usuário (estudante, professor, visitante) e o número de livros já emprestados.
tipo_usuario = input("Informe seu tipo de usuário (estudante, professor, visitante): ").strip().lower()
livros_emprestados = int(input("Informe o número de livros já emprestados: "))

# 2° Utilize estruturas de controle de fluxo (if, elif, else) para determinar se o usuário pode pegar mais livros emprestados ou se atingiu o limite.
if tipo_usuario == "estudante":
    limite = 3
elif tipo_usuario == "professor":
    limite = 5
elif tipo_usuario == "visitante":
    limite = 1
else:
    print("Tipo de usuário inválido.")
    limite = None
  
# 3° Exiba uma mensagem informando o resultado.
if limite is not None:
    if livros_emprestados < limite:
        livros_restantes = limite - livros_emprestados
        print(f"Você pode pegar mais {livros_restantes} livros emprestados.")
    else:
        print("Você atingiu o limite de livros emprestados.")
