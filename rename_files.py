# Este script renomeia todos os arquivos de um projeto que contêm um nome específico em seus nomes.
# Ele percorre recursivamente todos os diretórios e arquivos do caminho especificado e substitui o trecho 'old_name' pelo 'new_name' nos nomes dos arquivos.

import os

# Caminho do diretório onde os arquivos estão localizados
directory = 'caminho/do/projeto'

# Função para renomear arquivos
def rename_files(directory, old_name, new_name):
    """
    Renomeia arquivos em um diretório que contêm um nome específico.

    Args:
        directory (str): O caminho do diretório base.
        old_name (str): Nome ou parte do nome que será substituído.
        new_name (str): Novo nome ou parte do nome para substituição.

    Retorna:
        Nenhum. Os arquivos são renomeados diretamente no sistema de arquivos.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if old_name in file:  # Verifica se 'old_name' faz parte do nome do arquivo
                old_file = os.path.join(root, file)
                new_file = os.path.join(root, file.replace(old_name, new_name))
                os.rename(old_file, new_file)  # Renomeia o arquivo
                print(f'Renamed: {old_file} to {new_file}')  # Exibe o resultado no console

# Substitua 'nomeAntigoDoArquivo' e 'NovoNomeDoArquivo' pelos valores desejados
rename_files(directory, 'nomeAntigoDoArquivo', 'NovoNomeDoArquivo')
