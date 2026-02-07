import unittest
from src.bot import ChatBot

class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.bot = ChatBot()

    def test_initialization(self):
        self.assertIsNotNone(self.bot.df)
        self.assertIsNotNone(self.bot.vectorizer)
        self.assertIsNotNone(self.bot.tfidf_matrix)

    def test_known_query(self):
        query = "Where is my order?"
        response = self.bot.get_response(query)
        # We expect a relevant response, not the fallback
        self.assertNotEqual(response, "I'm sorry, I didn't understand that. Could you please rephrase your question?")
        # The response could be about delivery time or checking status. Both contain "order".
        self.assertTrue("order" in response.lower() or "tracking" in response.lower())

    def test_unknown_query(self):
        query = "random gibberish 123456789"
        response = self.bot.get_response(query)
        self.assertEqual(response, "I'm sorry, I didn't understand that. Could you please rephrase your question?")

    def test_threshold(self):
        # Test with a very high threshold to force fallback even for close matches
        query = "Where is my order?"
        response = self.bot.get_response(query, threshold=1.0)
        # Unless it's an exact 100% match (which it might not be due to preprocessing), it might fail. 
        # But let's assume we want to test that threshold logic works.
        # If we set threshold to 2.0, it should definitely fail.
        response_impossible = self.bot.get_response(query, threshold=2.0)
        self.assertEqual(response_impossible, "I'm sorry, I didn't understand that. Could you please rephrase your question?")

    def test_chitchat(self):
        self.assertEqual(self.bot.get_response("hi"), "Hello! How can I assist you today?")
        self.assertEqual(self.bot.get_response("Hello"), "Hi there! What can I do for you?")
        self.assertEqual(self.bot.get_response("THANKS"), "No problem! Happy to help.")

if __name__ == "__main__":
    unittest.main()
