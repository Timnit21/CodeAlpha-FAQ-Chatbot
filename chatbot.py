import json
import gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import time

# 1. Load data
with open('faq_data.json', 'r') as f:
    faqs = json.load(f)

questions = [q['question'].lower() for q in faqs]
answers = [q['answer'] for q in faqs]

# 2. Initialize Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(questions)

# 3. Core Logic
def get_bot_response(user_input, history):
    # Simulate thinking for better UX
    time.sleep(0.5) 
    
    user_vec = vectorizer.transform([user_input.lower()])
    similarities = cosine_similarity(user_vec, question_vectors).flatten()
    max_index = np.argmax(similarities)
    
    # Thresholding for accuracy
    if similarities[max_index] >= 0.2:
        return answers[max_index]
    return "I am unable to answer that specific query. Please reach out to services@codealpha.tech."

# 4. Interface (Stable version)
demo = gr.ChatInterface(
    fn=get_bot_response,
    title="🤖 CodeAlpha Pro Assistant",
    description="Your intelligent guide for CodeAlpha internship inquiries."
)

if __name__ == "__main__":
    demo.launch()