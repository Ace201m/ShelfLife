from django.contrib.syndication.views import Feed
from .models import feed
from . import views
from django.core.urlresolvers import reverse


class NewsFeed(Feed):
    title = "News"
    link = "/comments/"
    description = "Latest new articles"

    def items(self):
        return feed.objects.all().order_by("-time")[:5]

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content

    def item_date(self, item):
        return item.time

    def item_link(self, item):
        return reverse('basic:comment', kwargs={'id': item.pk})
