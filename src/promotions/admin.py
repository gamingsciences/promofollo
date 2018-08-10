from django.contrib import admin
from django.utils.html import format_html
from .models import Casino, Promotion

class CasinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)

    def url_(self, instance):
        return format_html('<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url))
    url_.allow_tags = True

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'casino', 'url_',)
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)
    readonly_fields = ['promo_image']
    
    def promo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )
    
    def url_(self, instance):
        return format_html('<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url))
    url_.allow_tags = True

admin.site.register(Casino, CasinoAdmin)
admin.site.register(Promotion, PromotionAdmin)
