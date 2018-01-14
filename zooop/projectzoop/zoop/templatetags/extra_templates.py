from django import template

register = template.Library()

@register.filter
def get_at_index(list, index):
    return list[index]

@register.filter
def get_details(object, index):
    return getattr(object, index)