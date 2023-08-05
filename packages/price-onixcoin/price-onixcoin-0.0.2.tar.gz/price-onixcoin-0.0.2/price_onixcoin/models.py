from django.db import models
from django.utils import timezone


# Create your models here.


class PriceBtcLocalbitcoin(models.Model):
    price_btc_usd_avg_1h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_usd_avg_6h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_usd_avg_12h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_usd_avg_24h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_bs_avg_1h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_bs_avg_6h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_bs_avg_12h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_bs_avg_24h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_price_btc'
        ordering = ['-created_at']


class PriceOnix(models.Model):
    btc_onx_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    onx_bs_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    usd_onx_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    btc_onx_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    onx_bs_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    usd_onx_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_historico_price'
        ordering = ['-created_at']


class Yobit(models.Model):
    btc_onx_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    usd_btc_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    btc_onx_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    usd_btc_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'yobit_onix'
        ordering = ['-created_at']
