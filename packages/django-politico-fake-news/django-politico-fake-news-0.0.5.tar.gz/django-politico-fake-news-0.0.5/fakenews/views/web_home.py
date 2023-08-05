from django.views.generic import TemplateView
from django.urls import reverse_lazy
from fakenews.authentication import secure


@secure
class WebHome(TemplateView):
    template_name = "fakenews/web-home.html"
    API_ROOT = reverse_lazy('api-root')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["API_ROOT"] = self.API_ROOT
        return context
