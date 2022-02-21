from django.urls import path
from .views import ContactListView, ContactDetailedView

urlpatterns = [
    path('contacts/', ContactListView.as_view()),
    path('contacts/<int:pk>', ContactDetailedView.as_view()),
]