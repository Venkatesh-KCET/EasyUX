from django import template

register = template.Library()

@register.filter(name='priority_color')
def priority_color(value):
    if value == 'High':
        return 'red'
    elif value == 'Medium':
        return 'orange'
    elif value == 'Low':
        return 'green'
    else:
        return 'black'