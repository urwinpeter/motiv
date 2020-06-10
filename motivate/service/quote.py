from motivate.models.database import QuotesDB
from pubsub import pub

class QuoteService():
    def __init__(self):
        self.quotes_db = QuotesDB()
 
    def get_quote(self):
        quote = self.quotes_db.get_quote()
        self._notify(quote)

    def _notify(self, quote):
        pub.sendMessage('quote_ready', quote=quote)