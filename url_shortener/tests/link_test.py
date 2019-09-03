from unittest import TestCase

from url_shortener.models.link import Link


def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]


class LinkTestCase(TestCase):

    def test_slug_is_different_from_url(self):
        link = Link(reverse, "some.long.url")
        self.assertNotEquals(link.slug, "some.long.url")

    def test_link_has_original_url(self):
        link = Link(reverse, "some.long.url")
        self.assertEqual(link.original_url, "some.long.url")
