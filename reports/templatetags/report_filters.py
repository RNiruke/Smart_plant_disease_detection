from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """Splits a string by the given argument."""
    if isinstance(value, str):
        return value.split(arg)
    return []
