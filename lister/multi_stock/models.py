from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from PIL import Image

CATEGORIES = (
    ('CLOTHING', 'Clothing'),
    ('ELECTRONICS', 'Electronics'),
    ('FURNITURE', 'Furniture'),
    ('TOYS', 'Toys'),
    ('MIXED GOODS', 'Mixed Goods'),
    ('RETURNS', 'Returns')
)


class StockListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        verbose_name=_("user"), 
        related_name='listings',
    )
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='stock_listings/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='MIXED GOODS')   
    phone = models.CharField(max_length=12)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    is_sold = models.BooleanField(_("is sold"), default=False, db_index=True)

    class Meta:
        verbose_name = _("listing")
        verbose_name_plural = _("listings")
        ordering = ['title', 'is_sold', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing_detail", kwargs={"pk": self.pk})
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)