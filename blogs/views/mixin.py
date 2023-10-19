from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from typing import Sequence
from django_htmx.http import trigger_client_event
from django.shortcuts import render


class TemplateLocationMixin(TemplateResponseMixin):
    template_location = None
    """Locate the template based on the url namespace."""

    def get_namespace(self) -> str:
        """Get the namespace base from the current path.

        Returns
        -------
        str
            /account/profile converted to app:account:profile
        """
        return resolve(self.request.path).namespace

    def get_template_location(self) -> str:
        """Get the template location base from the url namespace. Location of template should conform
        with the location url.

        Returns
        -------
        str
            Folder path URL namespace with `:` replaced with `/`
        """
        namespace = self.get_namespace()
        return namespace.replace(":", "/")

    def get_template_names(self) -> Sequence[str]:
        return [self.get_template()]

    def get_base_location(self) -> str:
        """Get the base location from the extracted namespace. There are currently two layout:
        account: Top Navigation
        manage: Fixed Sidebar

        Returns
        -------
        str
            The location of the base/partial templates - app/account/ or app/manage/
        """
        namespace = self.get_namespace()
        return "/".join(namespace.split(":")[0:2])

    def get_template(self) -> str:
        """Get the location of the render to be rendered. `template_location` specifies the location
        allowing reuse of template.

        Returns
        -------
        str
            The path of template.
        """
        if self.template_location:
            return f"{ self.template_location}/{self.template_name}"
        else:
            return f"{ self.get_template_location()}/{self.template_name}"


class HtmxResponseMixin(TemplateLocationMixin, ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context["base_template"] = f"{self.get_base_location()}/partial.html"
        else:
            context["base_template"] = f"{self.get_base_location()}/base.html"
        return context


class ModalMixin:
    modal_template = "blog/common/modal.html"
    modal_title = None
    modal_message = None
    modal_form_action = None
    modal_show = "modal-show"
    modal_hx_target = None
    modal_hx_swap = None
    modal_allowed_close = True
    modal_allowed_delete = False
    modal_submit_class = "btn btn-primary"
    modal_submit_value = "Submit"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        response = render(
            request,
            self.modal_template,
            context,
        )
        return trigger_client_event(response, self.modal_show)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.modal_title
        context["action"] = self.modal_form_action
        context["message"] = self.modal_message
        context["hx_target"] = self.modal_hx_target
        context["hx_swap"] = self.modal_hx_swap
        context["allowed_close"] = self.modal_allowed_close
        context["allowed_delete"] = self.modal_allowed_delete
        context["submit_class"] = self.modal_submit_class
        context["submit_value"] = self.modal_submit_value
        return context

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        context = self.get_context_data(form=form)
        response = render(
            self.request,
            self.modal_template,
            context,
        )
        return trigger_client_event(response, self.modal_show)
