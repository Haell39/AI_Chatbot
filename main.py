import gradio as gr
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt', quiet=True)




"""Definindo FAQs e respostas gerais para o chatbot""" 

# FAQs
faqs = {
    "What are your working hours?": "I'm here to help you 24/7!",
    "How can I track my order?": "You can track your order by clicking on the tracking link in your order confirmation email.",
    "Do you offer international shipping?": "Yes, we offer international shipping to most countries.",
    "What payment methods do you accept?": "We accept Visa, Mastercard, American Express, Discover, JCB, and Diners Club.",
    "How can I contact customer support": "You can reach us via email at support @example.com or by phone at 1-800-123-4567.",
    "Do you offer discounts?": "Yes, we offer discounts for students and senior citizens.",
    "Can I cancel my order?": "You can cancel your order within 24 hours of placing it.",
}


# Conversação geral:
general_chat = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hello! How can I help you?",
    "hey": "Hey! What can I do for you?",
    "how are you?": "I'm a bot, so I don't have feelings, but I'm here to help you!",
    "who are you?": "I'm a chatbot designed to help you with your questions!",
    "what are you?": "I'm a chatbot designed to help you with your questions!",
    "what can you do?": "I can help you with your questions!",
    "thanks": "You're welcome! Let me know if you need help with anything else!",
    "bye": "Goodbye! Have a great day!",
}

# Pré-processamento
all_questions = list(faqs.keys()) + list(general_chat.keys())
all_answers = list(faqs.values()) + list(general_chat.values())

# Vetorizando as perguntas (TF-IDF):
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(all_questions)



def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, faq_vectors).flatten()
    best_match_idx = np.argmax(similarities)
    
    return (
        all_answers[best_match_idx] 
        if similarities[best_match_idx] > 0.3 
        else "I'm sorry, I don't have an answer for that. Please contact support."
    )



# Interface Gradio
demo = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(placeholder="Type your question here...", label="Customer Support"),
    outputs=gr.Textbox(label="Response"),
    title="🤖 24/7 Customer Support Chatbot",
    description="Ask about shipping, payments, or just say hello!",
    examples=["How to track order?", "Do you offer discounts?", "Hi"],
    theme="soft"
)

demo.launch()