from celery.task import task
from django.db.models import Q
from dynamic_scraper.utils.task_utils import TaskUtils
from promotions.models import Casino, Promotion

@task
def run_spiders():
    print('running spiders')
    t = TaskUtils()
    t.run_spiders(Casino, 'scraper', 'scraper_runtime', 'promotion_spider')
