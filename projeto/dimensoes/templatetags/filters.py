from django import template

register = template.Library()


@register.filter
def arredonda(value, casas):
    return round(float(value), casas)
