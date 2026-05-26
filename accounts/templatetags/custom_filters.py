from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """
    Splits a string by a given separator/delimiter.
    Usage: {{ value|split:"," }}
    """
    return value.split(arg)
