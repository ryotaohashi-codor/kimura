from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Driver, Project

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

class DriverProjectListView(TemplateView):
    template_name = 'driver_project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        driver = get_object_or_404(Driver, pk=self.kwargs['pk'])
        context['driver'] = driver
        # ドライバーが関わったプロジェクトを重複なしで取得
        context['projects'] = Project.objects.filter(deliveries__driver=driver).distinct()
        return context