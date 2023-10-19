from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.views import generic
from django_htmx.http import HttpResponseLocation, trigger_client_event
from blogs.views.mixin import ModalMixin
from django import forms
from django.urls import reverse

from blogs.models import Comment, Blog


class Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class CreateView(LoginRequiredMixin, ModalMixin, generic.CreateView):
    template_name = "detail.html"
    model = Comment
    form_class = Form
    modal_title = "Create Comment"

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        self.object = None
        self.blog = Blog.objects.get(pk=self.kwargs.get("pk"))
        print("_" * 20)
        print(self.blog)
        return super().dispatch(request, *args, **kwargs)

    @property
    def modal_form_action(self):
        return self.blog.create_comment_url

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.blog = self.blog
        form.instance.blogger = self.request.user
        form.save()
        response = HttpResponseLocation(
            redirect_to=self.blog.get_absolute_url(),
            target="#content",
            swap="innerHTML",
        )
        return trigger_client_event(response, "modal-hide")
