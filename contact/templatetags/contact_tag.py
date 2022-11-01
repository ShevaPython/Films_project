from django import template
from contact.forms import ContactForm

register = template.Library()


@register.inclusion_tag('contact/tags/contact_email.html')
def contact_form():
    return {'form_contact': ContactForm}
