# Third party imports
from pubsub import pub
# Local application imports
from motivate.models.database import QuotesDB


class QuoteService():
    def __init__(self):
        self.quotes_db = QuotesDB()
 
    def get_quote(self):
        quote = self.quotes_db.get_quote()
        self._notify(quote)

    def _notify(self, quote):
        pub.sendMessage('quote_ready', quote=quote)