from django.shortcuts import redirect
from django.views.generic import CreateView


class OwnerCreateView(CreateView):

    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return redirect(self.redirect_name)
