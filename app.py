from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Link direto para os dados da planilha em CSV
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/1YxgYSwSwY6A6WjwmYr6LzDXEVxJCvL2e/export?format=csv&gid=1598712598"

@app.route('/')
def exibir_planilha():
    try:
        # Lê a planilha usando o pandas
        df = pd.read_csv(URL_PLANILHA)
        
        # Limpa nomes de colunas (remove espaços extras)
        df.columns = df.columns.str.strip()
        
        # Converte para uma lista de dicionários para o HTML ler fácil
        dados = df.to_dict(orient='records')
        
        return render_template('index.html', lista_dados=dados)
    
    except Exception as e:
        return f"Erro ao ler a planilha: {e}"

if __name__ == '__main__':
    app.run(debug=True)
