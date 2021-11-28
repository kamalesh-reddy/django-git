from django import template

register = template.Library()

@register.filter(name='cutit')
def cut(value,arg):
    return value.replace(arg,'')
