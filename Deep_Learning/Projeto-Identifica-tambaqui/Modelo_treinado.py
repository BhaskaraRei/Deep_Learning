import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carregar o modelo treinado
modelo = tf.keras.models.load_model("modelo_peixe.h5")

# Definir o tamanho das imagens
img_altura, img_largura = 150, 150

# Carregar a imagem para fazer a previsão
def classifica_img(caminho_imagen,imagen_altura,imagen_largura):
  img_path = caminho_imagen
  img = load_img(img_path, target_size=(imagen_altura, imagen_largura))
  img_array = img_to_array(img)
  img_array = np.expand_dims(img_array/255.0, axis=0)

  probabilidade = modelo.predict(img_array)
  predicao_classe = np.argmax(probabilidade, axis=1)
  liminar_confiaca = np.max(probabilidade,axis=1)
  if liminar_confiaca[0] > 0.8:
       classes = ['piranha', 'pirarucu', 'tambaqui', 'tucunare']
       return f"Classe prevista {classes[predicao_classe[0]]} "
  else:
       return f'Especie INDETERMINADA'

# Fazer a previsão

def testar_imagens():
    while True:
        caminho_img = input("\nDigite o caminho da imagem (ou 'sair'): ")
        # Se o usuário digitar 'sair', encerra o loop
        if caminho_img.lower() == 'sair':
            break
        
        # Chama a função de classificação
        resultado = classifica_img(caminho_img,img_altura,img_largura)
        print(f"Resultado: {resultado}")
        
        # Mostrar imagem
        # Lê a imagem usando OpenCV e converte para RGB para exibição correta
        img = cv2.cvtColor(cv2.imread(caminho_img), cv2.COLOR_BGR2RGB)
        plt.imshow(img) # Exibe a imagem usando Matplotlib
        plt.title(resultado) # Define o título da imagem com o resultado da classificação
        plt.axis('off') # Remove os eixos para uma visualização mais limpa
        plt.show() # Exibe a imagem com o resultado da classificação

testar_imagens()