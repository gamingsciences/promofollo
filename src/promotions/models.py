from django.db import models
import tagulous
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem


class Casino(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=30, blank=True)
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

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=200)
    casino = models.ForeignKey(Casino, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='promo_images', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    recuring = models.BooleanField(default=False)
    tags = tagulous.models.TagField(blank=True, null=True)
    reviewed = models.BooleanField(default=False)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class PromotionItem(DjangoItem):
    django_model = Promotion
