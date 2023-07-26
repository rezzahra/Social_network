from django.shortcuts import render
from django.views import View, generic


# Create your views here.

# class HomeView(View):
#     def get (self, request):
#         return render(request, 'home/index.html')
class HomeView(generic.TemplateView):
    template_name = 'home/index.html'