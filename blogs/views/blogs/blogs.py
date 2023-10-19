from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from blogs.views.mixin import HtmxResponseMixin
from blogs.models import Blog


class IndexView(LoginRequiredMixin, HtmxResponseMixin, generic.ListView):
    template_name = "index.html"
    model = Blog
    paginate_by = 5


class DetailView(LoginRequiredMixin, HtmxResponseMixin, generic.DetailView):
    template_name = "detail.html"
    model = Blog
