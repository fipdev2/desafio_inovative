from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)

# Caminho do CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), "Relatorio_cadop.csv")
CORS(app)  # Habilita requisições de outras origens

# Carregar o CSV corretamente
try:
    df = pd.read_csv(
        CSV_PATH,
        sep=';',  # O separador do CSV
        encoding='utf-8',
        dtype=str,  # Garante que não haja conversões erradas (exemplo: CNPJ em notação científica)
        quotechar='"',  # Tratar corretamente colunas com aspas
        skipinitialspace=True  # Remove espaços extras ao redor dos valores
    )
    df.fillna('', inplace=True)  # Substituir valores NaN por strings vazias
except Exception as e:
    print(f"Erro ao carregar CSV: {e}")
    df = pd.DataFrame()  # Cria um DataFrame vazio caso haja erro

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()  # Remove espaços extras

    if not query:
        return jsonify({"error": "No search query provided"}), 400

    if df.empty:
        return jsonify({"error": "No data available"}), 500

    # Busca em todas as colunas
    mask = df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False)).any(axis=1)
    results = df[mask].to_dict(orient='records')  # Retorna lista de dicionários corretamente formatada

    return jsonify(results)  # Flask automaticamente retorna um JSON válido

if __name__ == '__main__':
    app.run(debug=True)
