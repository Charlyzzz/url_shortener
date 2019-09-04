from django.test import TestCase
from url_shortener.models.link import Link
from unittest.mock import MagicMock


def new_link(url, hasher=lambda _: "slug", tracker=MagicMock()):
    return Link(url, hasher, tracker)


class LinkTestCase(TestCase):

    def test_slug_is_built_from_hasher(self):
        link = new_link("some.long.url")
        self.assertEqual(link.slug, "slug")

    def test_original_url_keeps_the_same(self):
        link = new_link("some.long.url")
        self.assertEqual(link.original_url, "some.long.url")

    def test_new_link_has_zero_views(self):
        link = new_link("some.long.url")
        self.assertEqual(link.view_count, 0)

    def test_track_view_increases_views_by_1(self):
        link = new_link("some.long.url")
        link.track_view()
        self.assertEqual(link.view_count, 1)

    # noinspection PyMethodMayBeStatic
    def test_track_view_reports_views_update(self):
        tracker = MagicMock()
        link = new_link("some.long.url", tracker=tracker)
        link.track_view()
        tracker.update_metrics.assert_called_once_with(link)
