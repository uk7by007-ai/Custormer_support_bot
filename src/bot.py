import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

class ChatBot:
    def __init__(self, data_path="data/faq.csv"):
        """
        Initialize the ChatBot by loading data and training the vectorizer.
        """
        self.data_path = data_path
        self.vectorizer = TfidfVectorizer()
        self.df = None
        self.tfidf_matrix = None
        self.load_data()
        self.chitchat_responses = {
            "hi": "Hello! How can I assist you today?",
            "hu": "Hello! How can I assist you today?",
            "hello": "Hi there! What can I do for you?",
            "hey": "Hey! Need any help with your order?",
            "how are you": "I'm just a bot, but I'm functioning perfectly! How can I help you?",
            "bye": "Goodbye! Have a great day!",
            "thank you": "You're welcome!",
            "thanks": "No problem! Happy to help."
        }

    def load_data(self):
        """
        Load FAQ data from CSV and prepare the TF-IDF matrix.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        
        try:
            self.df = pd.read_csv(self.data_path)
            # Ensure questions are strings
            self.df['question'] = self.df['question'].astype(str)
            
            # Train vectorizer on questions
            self.tfidf_matrix = self.vectorizer.fit_transform(self.df['question'])
            print("ChatBot initialized and data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.df = pd.DataFrame(columns=["question", "answer"])

    def get_response(self, user_query, threshold=0.3):
        """
        Get the best matching response for the user's query.
        """
        # Check for chit-chat first
        normalized_query = user_query.lower().strip()
        if normalized_query in self.chitchat_responses:
            return self.chitchat_responses[normalized_query]

        if self.df is None or self.df.empty:
            return "I'm sorry, my knowledge base is currently empty."

        # Transform user query
        query_vec = self.vectorizer.transform([user_query])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Find best match
        best_match_index = np.argmax(similarities)
        best_score = similarities[best_match_index]
        
        if best_score >= threshold:
            return self.df.iloc[best_match_index]['answer']
        else:
            return "I'm sorry, I didn't understand that. Could you please rephrase your question?"
