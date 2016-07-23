from django.conf.urls import url
from django.contrib import admin

import contacts.views

urlpatterns = [
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list', ),
    url(r'^edit/', contacts.views.CreateContactView.as_view(),
        name='contacts-edit', ),
]