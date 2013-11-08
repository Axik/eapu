from django.views.generic import ListView, TemplateView

from skd_tools.mixins import ActiveTabMixin

from cathedra.models import Lector


class LectorsListView(ActiveTabMixin, ListView):
    model = Lector
    active_tab = 'academics'


class HomeView(ActiveTabMixin, TemplateView):
    template_name = 'cathedra/home.html'
    active_tab = 'home'


lectors_list = LectorsListView.as_view()
home_view = HomeView.as_view()
