class Link:
    def __init__(self, hasher, original_link):
        self.original_url = original_link
        self.slug = hasher(original_link)
