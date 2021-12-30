from django.contrib.sitemaps import Sitemap
from .models import Debt, Booking

class DebtSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Debt.objects.all()

    def lastmod(self, obj):
        return obj.date

class BookingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Booking.objects.all()

    def lastmod(self, obj):
        return obj.date