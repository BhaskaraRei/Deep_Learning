import tensorflow as tf
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt
import numpy as np

# Definir o caminho do dataset
diretorio_treino = r'C:\Users\aluno noturno\Documents\Projeto-Identifica-tambaqui\fishes\train'
diretorio_validacao = r'C:\Users\aluno noturno\Documents\Projeto-Identifica-tambaqui\fishes\test'

# Definir o tamanho das imagens
img_altura, img_largura = 150, 150

# Processa 32 imagens por lote de uma vez
batch_size = 32

# Criar os geradores de imagens
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    diretorio_treino,
    target_size=(img_altura, img_largura),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    diretorio_validacao,
    target_size=(img_altura, img_largura),
    batch_size=batch_size,
    class_mode='categorical'
)

# Criar o modelo
modelo = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_altura, img_largura, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(4, activation='softmax')
])

# Compilar o modelo
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
treinamento = modelo.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator
)

loss, acuracia = modelo.evaluate(validation_generator)
print(f"Acuracia {acuracia * 100:.1f}")

# Usar o modelo para fazer previsões
def define_classe(caminho_imagen,imagen_altura,imagen_largura):
   img_path = caminho_imagen
   img = tf.keras.preprocessing.image.load_img(img_path, target_size=(imagen_altura, imagen_largura))
   img_array = tf.keras.preprocessing.image.img_to_array(img)
   img_array = np.expand_dims(img_array/255.0, axis=0)

   probabilidade = modelo.predict(img_array)
   predicao_classe = np.argmax(probabilidade, axis=1)
   liminar_confiaca = np.max(probabilidade,axis=1)
   if liminar_confiaca[0] > 0.8:
       classes = ['piranha', 'pirarucu', 'tambaqui', 'tucunare']
       return f"Classe prevista {classes[predicao_classe[0]]} "
   else:
       return f'Especie INDETERMINADO'

def testar_imagens():
    while True:
        caminho_img = input("\nDigite o caminho da imagem (ou 'sair'): ")
        # Se o usuário digitar 'sair', encerra o loop
        if caminho_img.lower() == 'sair':
            break
        
        # Chama a função de classificação
        resultado = define_classe(caminho_img,img_altura,img_largura)
        print(f"Resultado: {resultado}")
        
        # Mostrar imagem
        # Lê a imagem usando OpenCV e converte para RGB para exibição correta
        img = cv2.cvtColor(cv2.imread(caminho_img), cv2.COLOR_BGR2RGB)
        plt.imshow(img) # Exibe a imagem usando Matplotlib
        plt.title(resultado) # Define o título da imagem com o resultado da classificação
        plt.axis('off') # Remove os eixos para uma visualização mais limpa
        plt.show() # Exibe a imagem com o resultado da classificação

testar_imagens()

salva_modelo = input('Deseja salvar esse treinamento (Sim) ou (Nao) ?: ')

if salva_modelo.lower() == 'sim':
    modelo.save('modelo_salvo_peixe.h5')
    print('Modelo Salvo com sucesso')
else:
    print('Modelo não salvo, até logo...')