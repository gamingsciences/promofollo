import os
import datetime
from promofollo.settings.base import MEDIA_ROOT

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "promofollo.settings.base") #Changed in DDS v.0.3

BOT_NAME = 'promotions'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'promotions.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'promotions.scraper.pipelines.DjangoWriterPipeline': 800,
}

IMAGES_STORE = os.path.join(MEDIA_ROOT, 'promo_images')

IMAGES_THUMBS = {
    'medium': (350, 350),
    'small': (170, 170),
}

DSCRAPER_IMAGES_STORE_FORMAT = 'ALL'


DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'ERROR'
DSCRAPER_LOG_LIMIT = 5
