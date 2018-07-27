import datetime
from dynamic_scraper.spiders.django_spider import DjangoSpider
from promotions.models import Casino, Promotion, PromotionItem


class PromotionSpider(DjangoSpider):

    name = 'promotion_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Casino, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Promotion
        self.scraped_obj_item_class = PromotionItem
        super(PromotionSpider, self).__init__(self, *args, **kwargs)


class ArchivePromotionSpider(DjangoSpider):

    name = 'archive_promotion_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Casino, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = html_file
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Promotion
        self.scraped_obj_item_class = PromotionItem
        super(ArchivePromotionSpider, self).__init__(self, *args, **kwargs)
