# CodeAlpha Pro Assistant

An intelligent, retrieval-based FAQ Chatbot built to provide seamless assistance for CodeAlpha internship inquiries and technical knowledge.

## 🚀 Project Overview
The CodeAlpha Pro Assistant is a robust AI-driven tool designed to bridge the gap between prospective interns and company information. Utilizing a **Retrieval-Based Model** with **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**, the bot provides accurate, context-aware answers to user queries.

## 🛠 Technical Stack
* **Language:** Python 3.x
* **Interface:** Gradio (for a modern, responsive chat UI)
* **NLP Engine:** Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
* **Data Format:** JSON (for scalable knowledge management)

## 💡 Key Features
* **Scalable FAQ System:** Knowledge base is stored in a `faq_data.json` file, allowing for easy updates without modifying core logic.
* **Smart Matching:** Uses cosine similarity to find the most relevant response even when the user's input doesn't match the FAQ exactly.
* **Conversational UX:** Provides a professional chat interface with session history management and graceful fallback handling for unknown queries.
* **Separation of Concerns:** Modular design separating data ingestion, logic, and interface rendering.

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [Your-Repo-Link]
   cd CodeAlpha_FAQChatbot