import os
import pdfplumber
import pandas as pd
import zipfile

pdf_filename = None

# Verifica os arquivos na pasta 'anexos' e escolhe o primeiro que contém "Anexo_I_" e termina com ".pdf"
for filename in os.listdir("anexos"):
    if "Anexo_I_" in filename and filename.endswith(".pdf"):
        pdf_filename = os.path.join("anexos", filename)
        break

# Se não encontrar o PDF, gera um erro
if pdf_filename is None:
    raise FileNotFoundError("Nenhum arquivo PDF com 'Anexo_I_' encontrado na pasta 'anexos'.")

# Outros nomes de arquivos
csv_filename = "Rol_Procedimentos.csv"
zip_filename = "Teste_Filipe.zip"

# 🔹 2️⃣ Extração das tabelas do PDF
data = []

with pdfplumber.open(pdf_filename) as pdf:
    for page_num, page in enumerate(pdf.pages):
        # Lê o texto da página para procurar o título "Rol de Procedimentos e Eventos em Saúde"
        text = page.extract_text()
        
        if "Rol de Procedimentos e Eventos em Saúde" in text:
            print(f"Título encontrado na página {page_num + 1}")
            # Se encontrar o título, extrai as tabelas dessa página
            tables = page.extract_tables()
            for table in tables:
                # Adicionando todas as linhas da tabela
                if table:
                    data.extend(table)

# Verifica se encontrou dados
if not data:
    raise ValueError("Nenhuma tabela encontrada com o título 'Rol de Procedimentos e Eventos em Saúde'.")

# 🔹 3️⃣ Criando um DataFrame com as tabelas extraídas
df = pd.DataFrame(data)

# 🔹 4️⃣ Substituindo as abreviações "OD" e "AMB" pelas descrições completas
substituicoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

# Aplicando a substituição apenas nas colunas "OD" e "AMB"
df.replace(substituicoes, inplace=True)

# 🔹 5️⃣ Definindo o cabeçalho diretamente (não mantendo o cabeçalho numérico)
df.columns = df.iloc[0]  # Define a primeira linha como cabeçalho
df = df.drop(0).reset_index(drop=True)  # Remove a primeira linha que agora é o cabeçalho

# Salvando o DataFrame em formato CSV
df.to_csv(csv_filename, index=False, encoding="utf-8")

# Compactando o CSV em formato ZIP
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename)

print(f"Arquivo ZIP criado: {zip_filename}")
