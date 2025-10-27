'''Crie uma biblioteca com o nome do usuario e a hora local
e exiba na tela com uma mensagem'''



from datetime import datetime


nome = input("Qual é o seu nome? ")


hora_atual = datetime.now()


hora_formatada = hora_atual.strftime("%H:%M")


print(f"Oi,{nome} espero que esteja bem e esteja tendo um otimo dia meu guerreiro! A hora atual é {hora_formatada}.")