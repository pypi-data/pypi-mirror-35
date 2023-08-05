from django.views.generic import TemplateView
from django.urls import reverse_lazy
from fakenews.models import FactCheck
from fakenews.authentication import secure


@secure
class WebArticle(TemplateView):
    template_name = "fakenews/web-article.html"
    API_ROOT = reverse_lazy('api-root')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["API_ROOT"] = self.API_ROOT

        fc = FactCheck.objects.get()
        context["ARTICLE_ID"] = self.kwargs["slug"]
        return context
