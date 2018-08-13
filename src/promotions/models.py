from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
import tagulous
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem
from promofollo.settings.base import MEDIA_URL


class Casino(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    logo = models.ImageField(upload_to='casino_logos', blank=True, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    num_slots = models.IntegerField(default=0)
    num_table_games = models.IntegerField(default=0)
    num_hotel_rooms = models.IntegerField(default=0)
    poker = models.BooleanField(default=False)
    keno = models.BooleanField(default=False)
    bingo = models.BooleanField(default=False)

    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def get_logo(self):
        if self.logo:
            return mark_safe('<img src="%s" width=65 height=55/>' % self.logo.url)
        else:
            return 'No Logo Found'

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=200)
    casino = models.ForeignKey(Casino, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    image_file = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    recuring = models.BooleanField(default=False)
    tags = tagulous.models.TagField(blank=True, null=True)
    reviewed = models.BooleanField(default=False)
    date_created = models.DateField(default=timezone.now)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def image_full(self):
        if self.image_file:
            return mark_safe('<img src="%s" />' % "{}/{}/{}".format(MEDIA_URL,
                'promo_images/full', self.image_file))
        else:
            return 'No Image Found'

    def image_medium(self):
        if self.image_file:
            return mark_safe('<img src="%s" />' % "{}/{}/{}".format(MEDIA_URL,
                'promo_images/thumbs/medium', self.image_file))
        else:
            return 'No Image Found'

    def image_small(self):
        if self.image_file:
            return mark_safe('<img src="%s" />' % "{}/{}/{}".format(MEDIA_URL,
                'promo_images/thumbs/small', self.image_file))
        else:
            return 'No Image Found'

class PromotionItem(DjangoItem):
    django_model = Promotion
