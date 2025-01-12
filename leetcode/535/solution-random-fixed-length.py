import random
class Codec:
    storage = {}
    alphabet = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = ""
        while True:
            key = self.getKey()
            if key not in self.storage:
                break
        
        self.storage[key] = longUrl
        return "https://tinyurl.com/" + key
        
    def getKey(self):
        return ''.join([random.choice(self.alphabet) for i in range(0, 6)])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace("https://tinyurl.com/", "")
        return self.storage[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))