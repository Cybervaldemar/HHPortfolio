from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import TemplateView

from contacts.models import Contact, StudentOne
from contacts.models import Student

from contacts.pty.ptyParse import parse_pty


class IndexView(TemplateView):
    template_name = 'index.html'


class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class ListStudentsView(ListView):
    model = Student
    template_name = 'students_list.html'


class CreateContactView(CreateView):
    fields = ['first_name', 'last_name', 'email']
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

