# Detecção utilizando a rede YOLOv3

Este repositório foi criado para explorar o uso da técnica de **Detecção** utilizando redes de _Deep Learning_. Para isso, foi empregado o uso da rede detectora _YOLOv3_ da Darknet.

## Sobre o Projeto

O código feito para essa atividade está disponível no arquivo [detection_with_YOLOv3.ipynb](/./detection_with_YOLOv3/detection_with_YOLOv3.ipynb). Nele foi importado a rede YOLOv3 e aplicado o _Transfer Learning_, reutilizando os pesos da rede já treinada.

Para realizar o treinamento do modelo foi utilizado o dataset da [COCO](https://cocodataset.org/#home) de 2017, que possui 80 classes.

Ao fim do arquivo é feito um teste com uma imagem retirada da internet.

O arquivo com o código segue o exemplo dado no notebook [Tutorial_DarknetToColab](https://colab.research.google.com/drive/1lTGZsfMaGUpBG4inDIQwIJVW476ibXk_#scrollTo=j0t221djS1Gk), disponibilizado [nesse repositório](https://github.com/kriyeng/yolo-on-colab-notebook/).

### Objetivo

Este projeto foi desenvolvido como parte do desafio _Criação de Uma Base de Dados e Treinamento da Rede YOLO_ da trilha de aprendizado **BairesDev - Machine Learning Practitioner**, disponibilizado na plataforma [DIO](https://www.dio.me).
