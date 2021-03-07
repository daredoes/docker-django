from django import get_version
from django.views.generic import TemplateView, View, DetailView
from django.http import JsonResponse
from .tasks import show_hello_world
from .models import ItemModel
# Create your views here.


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo_content'] = ItemModel.objects.all()
        context['version'] = get_version()
        return context


class ItemDetailView(DetailView):

    model = ItemModel

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        output = obj.to_json()
        return JsonResponse(output)