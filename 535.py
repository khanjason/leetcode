class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        s="http://tinyurl.com/"
        s=s+longUrl
        return s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s=shortUrl[19:]
        return s
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
