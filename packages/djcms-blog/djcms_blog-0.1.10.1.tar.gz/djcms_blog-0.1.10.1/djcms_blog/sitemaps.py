from django.contrib.sitemaps import Sitemap

from .models import PostTitle


class PostsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return PostTitle.objects.filter(publisher_is_draft=False, published=True)
