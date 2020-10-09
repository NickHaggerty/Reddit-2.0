from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUser reationForm


cass SignUpView(CreationView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_view = 'signup.html'

