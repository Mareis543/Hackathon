from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# O link da sua planilha em formato CSV para facilitar a leitura
SHEET_URL = "https://docs.google.com/spreadsheets/d/1YxgYSwSwY6A6WjwmYr6LzDXEVxJCvL2e/export?format=csv"

@app.route('/')
def index():
    # 1. Lê os dados da planilha
    df = pd.read_csv(SHEET_URL)
    
    # 2. Converte para um formato que o HTML entende (lista de dicionários)
    dados_tabela = df.to_dict(orient='records')
    
    # 3. Envia para o HTML
    return render_template('index.html', dados=dados_tabela)

if __name__ == '__main__':
    app.run(debug=True)
