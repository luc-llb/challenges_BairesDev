# Recomendação de Produtos Baseada em Imagens

Sistema de recomendação que sugere produtos similares a partir de imagens utilizando técnicas de Deep Learning.

## 🎯 Sobre o Projeto

Este projeto implementa um sistema de recomendação de produtos baseado em similaridade visual utilizando redes neurais convolucionais. O sistema é capaz de classificar peças de roupa em 15 categorias diferentes e recomendar produtos similares disponíveis no Mercado Livre.

### 🚀 Principais Funcionalidades

- Classificação automática de peças de roupa em 15 categorias
- Extração de características visuais usando EfficientNetB7
- Recomendação de produtos similares via API do Mercado Livre
- Interface para upload e análise de imagens

### 🛠️ Tecnologias Utilizadas

- **TensorFlow/Keras**: Framework principal para deep learning
- **EfficientNetB7**: Arquitetura de rede neural pré-treinada com ImageNet
- **API Mercado Livre**: Integração para busca de produtos
- **Python**: Linguagem de programação principal
- **Jupyter Notebook**: Ambiente de desenvolvimento

## 📊 Dataset

O projeto utiliza o [Clothes-dataset](https://www.kaggle.com/datasets/ryanbadai/clothes-dataset) disponível no Kaggle, que contém imagens de roupas classificadas em 15 categorias diferentes.

## 📝 Metodologia

O projeto foi desenvolvido em duas etapas principais:

1. **Treinamento do Modelo**:

   - Utilização da EfficientNetB7 pré-treinada
   - Fine-tuning para classificação de roupas
   - Baseado no trabalho de [Ashik Shahriar](https://www.kaggle.com/ashikshahriar)

2. **Sistema de Recomendação**:
   - Extração de features das imagens
   - Cálculo de similaridade entre produtos
   - Integração com API do Mercado Livre

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte do desafio "Criando um Sistema de Recomendação por Imagens Digitais" da trilha **BairesDev - Machine Learning Practitioner** na plataforma [DIO](https://www.dio.me).

## 📚 Referências

- [Clothes Classification Notebook](https://www.kaggle.com/code/ashikshahriar/clothes-classification)
- [ImageNet Dataset](https://www.image-net.org)
- [Documentação API Mercado Livre](https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br)
