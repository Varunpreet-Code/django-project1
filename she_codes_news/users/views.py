from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name ='users/Profile.html'
    context_object_name = 'UserDetails'

# def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
#         context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
#         return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        print(context)
        return context

# Create your views here.
