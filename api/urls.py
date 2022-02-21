from django.urls import path, re_path
from .views import ContactListView, ContactDetailedView

urlpatterns = [
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('contacts/<int:pk>', ContactDetailedView.as_view(), name="contacts_detail"),
]