from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
	"""
	This cuts out all vlues of "arg" rom the string!
	"""

	return value.replace(arg,'')

# register.filter('cut',cut)