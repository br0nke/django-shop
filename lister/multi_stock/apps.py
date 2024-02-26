from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MultiStockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'multi_stock'

    class Meta:
        verbose_name = _('multi stock')