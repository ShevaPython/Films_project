import requests

from .service import send
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm


class ContactView(CreateView):
    model = Contact
    fields = ['email']
    success_url = '/'
    template_name = 'films/movies_list.html'

    def form_valid(self, form):

        form.save()
        send(form.instance.email)
        return super().form_valid(form)
