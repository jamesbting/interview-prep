import random
class Codec:
    storage = {}
    i = 0


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.storage[self.i] = longUrl
        self.i += 1
        return "https://tinyurl.com/" + str(self.i - 1)
    

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = int(shortUrl.replace("https://tinyurl.com/", ""))
        return self.storage[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))