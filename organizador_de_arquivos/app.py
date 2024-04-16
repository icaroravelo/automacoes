import os
import shutil
import time

def organizador(pasta_de_download):
    # Lista todos os arquivos na pasta de downloads
    arquivos = os.listdir(pasta_de_download)

    # Loop através de cada arquivo na pasta
    for arquivo in arquivos:
        # Ignorar diretórios
        if os.path.isdir(os.path.join(pasta_de_download, arquivo)):
            continue

        # Esperar um curto período de tempo para dar a chance do arquivo ser liberado
        time.sleep(0.5)

        # Tentar mover o arquivo
        try:
            # Obter a extensão do arquivo
            _, extensão = os.path.splitext(arquivo)

            # Criar o diretório para a extensão se não existir
            diretorio_de_destino = os.path.join(pasta_de_download, extensão[1:].lower())
            if not os.path.exists(diretorio_de_destino):
                os.makedirs(diretorio_de_destino)

            # Mover o arquivo para o diretório correspondente
            shutil.move(os.path.join(pasta_de_download, arquivo), diretorio_de_destino)
            print(f"Arquivo '{arquivo}' movido com sucesso.")
        except Exception as e:
            print(f"Não foi possível mover o arquivo '{arquivo}': {e}")

    print("Organização concluída!")

if __name__ == "__main__":
    pasta_de_download = "C:\\Users\\regul\\Downloads"
    organizador(pasta_de_download)
