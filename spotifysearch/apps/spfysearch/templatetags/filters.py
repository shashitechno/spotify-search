from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css):
    if field:
        return field.as_widget(attrs={"class":css})
    else:
        return ''