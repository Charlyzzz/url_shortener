def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]


class Link:
    def __init__(self, original_link, hasher, tracker):
        self.original_url = original_link
        self.slug = hasher(original_link)
        self.view_count = 0
        self.tracker = tracker

    def track_view(self):
        self.increase_view_count()

    def increase_view_count(self):
        self.view_count += 1
        self.tracker.update_metrics(self)
