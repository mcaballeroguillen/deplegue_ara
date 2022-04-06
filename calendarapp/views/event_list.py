from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from calendarapp.models import Event, EventMember


class AllEventsListView(ListView):
    """ All event list views """
    template_name = 'calendarapp/events_list.html'
    model = Event

    def get_queryset(self):
        object_list=[]
        normales = Event.objects.filter(user=self.request.user)
        extra = EventMember.objects.filter(user=self.request.user)
        for e in normales:
            evento_detallado= Event.objects.get(id=e.id)
            object_list.append(evento_detallado)
        for e in extra:
            evento_detallado = Event.objects.get(id=e.event_id)
            object_list.append(evento_detallado)

        return object_list


class RunningEventsListView(TemplateView):
    """ Running events list view """
    template_name = 'calendarapp/events_list.html'
    model = EventMember
    def get(self, request, *args, **kwargs):
        Evento_extra = EventMember.objects.filter(user=self.request.user)
        object_list =[]
        for evento in Evento_extra:
            detallado= Event.objects.get(id=evento.event_id)
            object_list.append(detallado)
        Eventos_Normales= Event.objects.filter(user=self.request.user)
        for e in Eventos_Normales:
            object_list.append(e)
        ctx = {'object_list': object_list}
        return render(request,'calendarapp/events_list.html',ctx)



