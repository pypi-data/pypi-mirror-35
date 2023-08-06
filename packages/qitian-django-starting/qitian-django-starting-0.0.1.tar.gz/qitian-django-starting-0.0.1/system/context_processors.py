from django.conf import settings
from .models import SiteProperty, Links
import random


def site_info(request):
    site_property = SiteProperty.objects.filter(site__domain=request.site.domain).first()
    links = Links.objects.filter(status=1).filter(site=request.site).all()
    return {
        'site': site_property,
        'links': links,
        'version': settings.STATIC_VERSION if not settings.DEBUG else random.randint(10000, 999999),
    }
