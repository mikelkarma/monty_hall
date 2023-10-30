from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Função para simular o problema de Monty Hall
def simulate_monty_hall(num_simulations):
    keep_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        car_behind = random.randint(1, 3)
        choice = random.randint(1, 3)

        # Monty abre uma porta com uma cabra
        doors_with_goats = [door for door in [1, 2, 3] if door != choice and door != car_behind]
        monty_opens = random.choice(doors_with_goats)

        # Decide se o jogador mantém ou troca
        switch = [door for door in [1, 2, 3] if door != choice and door != monty_opens][0]

        if switch == car_behind:
            switch_wins += 1
        elif choice == car_behind:
            keep_wins += 1

    return keep_wins, switch_wins


# Rota principal para a simulação de Monty Hall
@app.route('/', methods=['GET', 'POST'])
def monty_hall_simulation():
    if request.method == 'POST':
        # Obtém o número de simulações do formulário
        num_simulations = int(request.form['num_simulacoes'])
        # Limita o número máximo de simulações a 10.000
        num_simulations = min(num_simulations, 10000)
        # Realiza a simulação e obtém as porcentagens de vitória
        keep_wins, switch_wins = simulate_monty_hall(num_simulations)
        
        # Calcula as porcentagens corretas
        keep_percentage = (keep_wins / num_simulations) * 100
        switch_percentage = (switch_wins / num_simulations) * 100

        # Retorna os resultados em formato JSON
        return jsonify({"num_simulations": num_simulations, "keep_percentage": keep_percentage, "switch_percentage": switch_percentage})
    else:
        # Configura o número de simulações padrão
        num_simulations = 10000
        # Renderiza a página inicial com os valores iniciais
        return render_template('index.html', num_simulations=num_simulations)

if __name__ == '__main__':
    app.run(debug=True)
