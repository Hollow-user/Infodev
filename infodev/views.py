from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from django.core.paginator import Paginator
from rest_framework.generics import ListCreateAPIView
from .serializers import DeviceSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .forms import *


class PageOne(View):

    def get(self, request):
        device = CommunicationDevice.objects.all()
        paginator = Paginator(device, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginator = page.has_other_pages()

        return render(
            request,
            'infodev/main.html',
            context={'page': page, 'is_paginated': is_paginator}
        )

    def post(self, request):

        if 'device_id' in request.POST:
            one_device = CommunicationDevice.objects.get(id=request.POST['device_id'])
            if one_device.active:
                CommunicationDevice.objects.filter(
                    id=request.POST['device_id']).update(active=False)
                message = 'Устройство отключено'
            else:
                CommunicationDevice.objects.filter(
                    id=request.POST['device_id']).update(active=True)
                message = 'Устройство включено'

        return render(request, 'infodev/message.html', context={'message': message})


class MessageView(View):
    def get(self, request):
        message = 'Сообщение'
        return render(request, 'infodev/message.html', context={'message': message})


class AddDevice(View):
    def get(self, request):
        form = DeviceForm
        return render(request, 'infodev/add_device.html', {'form': form})

    def post(self, request):
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            message = 'Устройство добавлено'
            return redirect('device_url', id=device.id)


class OneDevice(View):
    def get(self, request, id):
        device = get_object_or_404(CommunicationDevice, id=id)
        return render(
            request,
            'infodev/device.html',
            context={'device_id': id, 'device': device}
        )

    def post(self, request, id):
        one_device = CommunicationDevice.objects.get(id=id)
        if one_device.active:
            CommunicationDevice.objects.filter(
                id=id).update(active=False)
            message = 'Устройство отключено'
        else:
            CommunicationDevice.objects.filter(
                id=id).update(active=True)
            message = 'Устройство включено'
        return render(request, 'infodev/message.html',
                      context={'message': message})


class DeviceView(ListCreateAPIView):
    queryset = CommunicationDevice.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['device_type']
    search_fields = [
            'device_type',
            'address',
            'Latitude',
            'Longitude',
            'radius',
            'active'
    ]
