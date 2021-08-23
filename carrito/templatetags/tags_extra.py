from django import template

register = template.Library()
 
@register.filter(name='getvalue')
def getvalue(dictionary, key):
    return dictionary.get(key)

register.filter('getvalue', getvalue)