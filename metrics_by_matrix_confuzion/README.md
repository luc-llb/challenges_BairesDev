# Obtendo as métricas pela Matriz de Confusão

Este repositório foi criado para explorar a obtenção das métricas de avaliação de aprendizado para um modelo de Machine Learning baseado na **Matriz de Confusão** gerada pela resposta do modelo para os dados de teste.

## Sobre o Projeto

O código feito para essa atividade está disponível no arquivo [metrics_by_matrix_confuzion.ipynb](/metrics_by_matrix_confuzion.ipynb). Nele foi implementado uma rede neural classificadora com 3 camadas utilizando o _TensorFlow_ e o dataset do _MNIST_, enquanto a biblioteca _Scikit-learn_ foi utilizada para se obter a Matriz de Confusão.

Com o modelo treinado foi obtida a Matriz de Confusão proveniente do mesmo e então as métricas de Acurácia, Precisão, Recall, Especificidade e F-Score. Sendo calculados pelas formulas:

- Acurácia: (TP + TN) / (TP + TN + FP + FN)
- Precisão: TP / (TP + FP)
- Recall: TP / (TP + FN)
- Especificidade: TN / (TN + FP)
- F1 Score: (2 * Precision * Recall) / (Precision + Recall)

Ao fim do arquivo é feito um comparativo entre os valores obtidos manualmente, calculados pela matriz de confusão com as formulas acima, e os valores obtidos de métodos já implementados nas bibliotecas _scikit-learn_ e _imbalanced-learn_.

### Objetivo

Este projeto foi desenvolvido como parte do desafio _Cálculo de Métricas de Avaliação de Aprendizado_ da trilha de aprendizado **BairesDev - Machine Learning Practitioner**, disponibilizado na plataforma [DIO](https://www.dio.me).
