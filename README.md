# Como funciona:
Este site simula o problema de Monty Hall, um quebra-cabeça de probabilidade nomeado após o apresentador do programa de televisão "Vamos Fazer um Negócio", Monty Hall.

O problema envolve três portas, sendo que atrás de uma delas há um carro e atrás das outras duas há cabras. Você escolhe uma porta e, em seguida, Monty, que sabe o que há atrás de cada porta, abre outra porta revelando uma cabra. Você tem a opção de manter sua escolha inicial ou trocar para a porta não aberta restante. Esta simulação calcula as probabilidades para ambas as estratégias.


# Explicão do cauculo
```python
 def simular_monty_hall(num_simulacoes):
    # Inicializa as contagens de vitórias ao manter a escolha original e ao trocar
    vitorias_mantendo = 0
    vitorias_trocando = 0

    # Realiza o número de simulações especificado
    for _ in range(num_simulacoes):
        # Escolhe aleatoriamente uma porta onde o carro está
        carro_por_tras = random.randint(1, 3)
        # O jogador faz uma escolha aleatória de uma das três portas
        escolha = random.randint(1, 3)

        # Monty Hall abre uma porta com uma cabra
        portas_com_cabras = [porta for porta in [1, 2, 3] if porta != escolha and porta != carro_por_tras]
        monty_abre = random.choice(portas_com_cabras)

        # O jogador decide se quer manter sua escolha original ou trocar
        troca = [porta for porta in [1, 2, 3] if porta != escolha and porta != monty_abre][0]

        # Verifica se o jogador ganhou mantendo sua escolha original ou trocando
        if troca == carro_por_tras:
            vitorias_trocando += 1
        elif escolha == carro_por_tras:
            vitorias_mantendo += 1

    # Retorna o número de vitórias ao manter a escolha original e ao trocar
    return vitorias_mantendo, vitorias_trocando
```
