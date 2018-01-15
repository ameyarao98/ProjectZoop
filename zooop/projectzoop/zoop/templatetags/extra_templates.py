from django import template

register = template.Library()

@register.filter
def get_at_index(list, index):
    return list[index]

@register.filter
def get_details(object, index):
    return getattr(object, index)

@register.filter
def get_item(dictionary, key):
    print(dictionary)
    return dictionary.get(key)

@register.filter
def get_count_list(dictionary, postid):
    count_list = [v for k,v in dictionary.items() if k[0]==postid]
    return count_list
