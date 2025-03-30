import os
import requests
import zipfile
from bs4 import BeautifulSoup

# URL da página
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Pasta para armazenar os PDFs
PASTA_DOWNLOADS = "anexos"
os.makedirs(PASTA_DOWNLOADS, exist_ok=True)

# Fazer a requisição para obter o HTML
def baixar_pagina(url):
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.text

# Extrair os links dos anexos I e II
def extrair_links_pdfs(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        # print('href ====>', href)
        # print('link ====>', link)
        
        if "Anexo I" in link.getText() or "Anexo II" in link.getText():
            if href.endswith('.pdf'):
                links.append(href)
    return links

# Baixar os PDFs
def baixar_pdfs(links):
    arquivos_baixados = []
    for link in links:
        nome_arquivo = os.path.join(PASTA_DOWNLOADS, link.split("/")[-1])
        resposta = requests.get(link)
        with open(nome_arquivo, "wb") as f:
            f.write(resposta.content)
        arquivos_baixados.append(nome_arquivo)
    return arquivos_baixados

# Compactar os PDFs em um único ZIP
def compactar_arquivos(arquivos, nome_zip="anexos.zip"):
    with zipfile.ZipFile(nome_zip, "w") as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))

if __name__ == "__main__":
    html = baixar_pagina(URL)
    links_pdfs = extrair_links_pdfs(html)
    if links_pdfs:
        print("Baixando arquivos...")
        arquivos_baixados = baixar_pdfs(links_pdfs)
        print("Compactando arquivos...")
        compactar_arquivos(arquivos_baixados)
        print("Processo concluído! Arquivo ZIP gerado.")
    else:
        print("Nenhum anexo encontrado.")
