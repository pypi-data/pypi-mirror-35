from django.contrib.sitemaps import Sitemap

from .models import Page


class PagesSitemap(Sitemap):
    """Sitemap class for the simple_pages app."""
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        """Gets a list of items to be displayed in the sitemap."""
        return Page.objects.filter(enabled=True)

    def lastmod(self, obj):
        """Uses this date to determine when a Page was last modified."""
        return obj.modified
