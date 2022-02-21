from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
import re

# Create your views here.
class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    #  Overriding post method to check if we already have this contact's details
    #  Also checking if the phone number is valid
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            phone_number = serializer.validated_data['phone_number']
            email = serializer.validated_data['email']

            phone_number_regex = "([0-9]|[\-+#]*)"

            #  We create a dict for error message to be able to return multiple error messages
            error_messages = {}

            if re.match(phone_number, phone_number_regex):
                error_messages['phone_number_validation'] = 'number can contain only numbers and symbols'
            if Contact.objects.filter(name=name).exists():
                error_messages['name'] = 'Another contact has this name'
            if Contact.objects.filter(phone_number=phone_number).exists():
                error_messages['phone_number'] = 'Another contact has this phone number'
            if Contact.objects.filter(email=email).exists():
                error_messages['email'] = 'Another contact has this email'

            if len(error_messages) == 0:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    #  Overriding put method to check if updated details exist in other contacts
    #  Also checking if the phone number is valid
    def put(self, request, *args, **kwargs):
        contact = self.get_object()
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():

            # When updating an existing contact, we'll always find contact (that contact itself) that has
            # some of the same details, so we need to allow some duplicates, depending on what we're updating
            name_allowed_duplicates = 0
            phone_allowed_duplicates = 0
            email_allowed_duplicates = 0

            pk = kwargs['pk']
            name = serializer.validated_data['name']
            phone_number = serializer.validated_data['phone_number']
            email = serializer.validated_data['email']

            phone_number_regex = "([0-9]|[\-+#]*)"

            # We'll check here which new data is the same as the old data and assign allowed duplicates
            if name == Contact.objects.get(pk=pk).name:
                name_allowed_duplicates = 1
            if phone_number == Contact.objects.get(pk=pk).phone_number:
                phone_allowed_duplicates = 1
            if email == Contact.objects.get(pk=pk).email:
                email_allowed_duplicates = 1

            #  We create a dict for error message to be able to return multiple error messages
            error_messages = {}

            if re.match(phone_number, phone_number_regex):
                error_messages['phone_number_validation'] = 'number can contain only numbers and symbols'
            if Contact.objects.filter(name=name).count() > name_allowed_duplicates:
                error_messages['name'] = 'Another contact has this name'
            if Contact.objects.filter(phone_number=phone_number).count() > phone_allowed_duplicates:
                error_messages['phone_number'] = 'Another contact has this phone number'
            if Contact.objects.filter(email=email).count() > email_allowed_duplicates:
                error_messages['email'] = 'Another contact has this email'

            if len(error_messages) == 0:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)