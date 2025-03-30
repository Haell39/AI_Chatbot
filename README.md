# 🤖 Customer Support Chatbot with NLP & Gradio

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-Interface-orange?logo=gradio)](https://gradio.app)
[![NLTK](https://img.shields.io/badge/NLP-NLTK-green?logo=nltk)](https://nltk.org)

![Chatbot Demo](files\chatbot.gif) <!-- Substitua por seu GIF/Imagem -->

## 📌 Overview
Chatbot inteligente para atendimento ao cliente que combina:
- **Processamento de Linguagem Natural (NLP)** com NLTK
- **Matching de perguntas** usando TF-IDF e Cosine Similarity
- **Interface interativa** com Gradio

> ✨ **Destaque técnico**: Sistema híbrido que trata tanto FAQs estruturadas quanto conversação casual com threshold de confiança ajustável.

<br>

## 🛠️ Tecnologias
| Tecnologia | Função | 
|------------|--------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Linguagem principal |
| ![Gradio](https://img.shields.io/badge/-Gradio-FF4B4B?logo=gradio&logoColor=white) | Interface web |
| ![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white) | TF-IDF & Cosine Similarity |
| ![NLTK](https://img.shields.io/badge/-NLTK-40A351?logo=nltk&logoColor=white) | Tokenização/Pontuação |

<br>

## 🎯 Features
1. **Resposta a FAQs**  
   - Rastreamento de pedidos  
   - Formas de pagamento  
   - Suporte internacional  

2. **Small Talk**  
   - Cumprimentos (`hi`, `hello`)  
   - Perguntas sobre o bot (`who are you?`)  

3. **Fallback Seguro**  
   - Resposta padrão para perguntas desconhecidas  

<br>

## 📦 Instalação
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/customer-support-chatbot.git

# 2. Crie o ambiente Conda
conda env create -f environment.yml

# 3. Ative o ambiente
conda activate chatbot-env

# 4. Execute o chatbot
python src/app.py
```

<br>

## 🖥️ Como Usar
1. O chatbot iniciará automaticamente em:  
   `http://127.0.0.1:7860`  
2. Digite perguntas como:
   - *"How can I track my order?"*
   - *"Do you offer discounts?"*
   - *"Hello!"*

![Exemplo de Conversação](files\image.png) <!-- Adicione screenshot -->

<br>

## 🧠 Arquitetura
```
graph TD
    A[User Input] --> B[Text Preprocessing]
    B --> C[TF-IDF Vectorization]
    C --> D[Cosine Similarity]
    D --> E{Similarity > 0.3?}
    E -->|Yes| F[Select Best Match]
    E -->|No| G[Fallback Response]
    F --> H[FAQ Response]
    F --> I[General Chat Response]
    H -->|"Ex: Tracking info"| J[Output]
    I -->|"Ex: Hello!"| J
    G -->|"I don't know..."| J
```


<br>



## 🤝 Contribuição
Contribuições são bem-vindas! Siga estes passos:
1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Add some feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

<br>

## 📄 Licença
Distribuído sob licença MIT. Veja `LICENSE` para mais informações.

---
  
> ✉ **Contato**: Rafael A. Dutra - rafaeldutrapro@gmail.com  
> 🌐 **LinkedIn**: [rafaelsantoshome](https://www.linkedin.com/in/rafaelsantoshome/)
