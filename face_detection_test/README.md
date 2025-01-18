# Detecção Faces utilizando a YOLOv5

Este repositório foi criado para explorar o uso da técnica de **Detecção** utilizando redes de _Deep Learning_. Para isso, foi empregado o uso da rede detectora _YOLOv5_ da [Ultralytics](https://ultralytics.com/).

## Sobre o Projeto

O código feito para essa atividade está disponível no arquivo [face_detection.ipynb](/./face_detection_test/face_detection.ipynb). Nele foi importada a rede YOLOv5 e aplicado o _Transfer Learning_, reutilizando os pesos da rede _YOLOv5s_.

O principal foco desse treinamento é realizar a detecção e classificação das faces das pessoas nas imagens, focando-se em classificar os personagens do seriado, **House** e **Cuddy**. Demais pessoas que aparecerem nas imagens são classificadas como **Outros**.

O arquivo com o código segue a que é dito no [nesse guia](https://docs.ultralytics.com/pt/yolov5/tutorials/train_custom_data/) disponibilizado pela Ultralytics.

### Dataset Utilizado

Para realizar o treinamento do modelo foi criado um dataset, disponível no arquivo [dataset.zip](/./face_detection_test/dataset.zip), que contem 200 imagens, sendo metade delas focadas no ator Hugh Laurie (House) e a outra metade focada na atriz Lisa Edelstein (Cuddy), que compõe o elenco da série House M.D.

Todas as imagens foram obtidas do site [Gettyimages](https://www.gettyimages.com.br), com excessão da imagem de teste, utilizada ao fim do arquivo, que foi obtida no site [techtudo](https://www.techtudo.com.br/guia/2023/11/dr-house-relembre-historia-e-elenco-da-serie-medica-dos-anos-2000-streaming.ghtml).

### Objetivo

Este projeto foi desenvolvido como parte do desafio _Criando um Sistema de Reconhecimento Facial do Zero_ da trilha de aprendizado **BairesDev - Machine Learning Practitioner**, disponibilizado na plataforma [DIO](https://www.dio.me).
