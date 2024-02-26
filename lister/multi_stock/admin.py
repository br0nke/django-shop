from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class StockListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'phone', 'category', 'is_sold')
    list_filter = ['is_sold', 'owner', 'created_at', 'category']

    def total_listings(self, obj: models.StockListing):
        return obj.listings.count()
    total_listings.short_description = _('total listings')

    def sold_listings(self, obj: models.StockListing):
        return obj.listings.filter(is_done=True).count()
    sold_listings.short_description = _('sold listings')

admin.site.register(models.StockListing, StockListingAdmin)