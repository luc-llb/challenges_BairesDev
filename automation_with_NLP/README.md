# Assistente Virtual Controlado por Voz - Assis

Sistema de assistência virtual que automatiza alguns processos por meio de pedidos falados pelo usuário.

## 🎯 Sobre o Projeto

Este projeto implementa um assistente virtual, chamada Assis, que executa ações por meio da fala e responde ao usuário. O sistema é capaz de executar algumas ações pre programadas.

O foco do projeto era a utilização do _Processamento de Linguagem Natural (PLN)_ aplicando-o em um sistema real. O PLN é feito pelas bibliotecas **Speech Recognition** e **Edge TTS**.

### 🚀 Principais Funcionalidades

- Transformação de texto para fala (_text-to-speach_) para responder e instruir o usuário
- Transformação de fala para texto (_speach-to-text_) para facilitar a utilização pelo usuário
- No navegador: fornece pesquisas no _Google_ e _YouTube_, além de também fechar o navegador se solicitado
- Conta piadas, informa o horário e pode encerrar a própria execução

### 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para a implementação de todo o sistema
- **Speech Recognition**: Biblioteca para realizar o reconhecimento de fala, com suporte para vários motores e APIs, online e offline
- **Edge TTS**: Módulo Python que permite que você use o serviço de texto em fala on-line da Microsoft Edge de dentro do seu código Python
- **Joke API**: API de piadas com suporte a língua portuguesa

### 💻 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/luc-llb/challenges_BairesDev.git
```

2. Acesse a pasta desse projeto:

```bash
cd challenges_BairesDev/automation_with_NLP/
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Como é feito o uso da biblioteca Pydub para reprodução do áudio é necessário instalar o [FFmpeg](https://ffmpeg.org/download.html). Para instala-lo no Windows siga [esse tutorial](https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows). Já no Linux/MacOS, utilize os seguintes comandos no terminal:

```bash
sudo apt install ffmpeg  # Debian/Ubuntu
brew install ffmpeg      # macOS
```

5. Execute o código no arquivo .py:

```bash
python assis.py
```

## 📝 Metodologia

O projeto foi desenvolvido com foco em 3 módulos, as funções:

- `speak()`: Que é responsavel pela transformação do texto para áudio, dando voz ao nosso assistente.
- `get_order()`: Responsavel por obter o pedido para o assistente, transformando o audio capturado em fala.
- `respond()`: Responsavel pela execução dos pedidos feitos ao assistente.

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte do desafio "Criando um sistema de assistência virtual do zero" da trilha **BairesDev - Machine Learning Practitioner** na plataforma [DIO](https://www.dio.me).

## 📚 Referências

- [EdgeTTS](https://github.com/rany2/edge-tts)
- [Código do professor Diego Bruno](https://github.com/diegobrunoDIO/Speech-to-text-ML-DIO/tree/main)
- [Joke API](https://sv443.net/jokeapi/v2/)
