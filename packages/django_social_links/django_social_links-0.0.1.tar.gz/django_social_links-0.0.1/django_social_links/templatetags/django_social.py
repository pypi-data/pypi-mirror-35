from django import template
from django_social_links.models import SocialNetwork

register = template.Library()


@register.simple_tag
def get_social_links():
    return SocialNetwork.objects.all()
