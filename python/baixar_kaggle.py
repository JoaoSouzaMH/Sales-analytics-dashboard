import os
from kaggle.api.kaggle_api_extended import KaggleApi

# 🔑 coloque aqui seus dados (NÃO compartilhe com ninguém)
os.environ['KAGGLE_USERNAME'] = 'joosouzamh'
os.environ['KAGGLE_KEY'] = '8802a4d0f35d22c04de57ca5c35baf01'

api = KaggleApi()
api.authenticate()

print("Conectado com sucesso!")

api.dataset_download_files(
    "olistbr/brazilian-ecommerce",
    path="./dados",
    unzip=True
)

print("Download concluído!")