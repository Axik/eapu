from django.views.generic import TemplateView

from skd_tools.mixins import ActiveTabMixin

from cathedra.models import Lector, Aspirant, Technician


class LectorsListView(ActiveTabMixin, TemplateView):
    template_name = 'cathedra/lector_list.html'
    active_tab = 'academics'

    def get_context_data(self, **kwargs):
        context = super(LectorsListView, self).get_context_data(**kwargs)
        context['lectors'] = Lector.objects.all()
        context['aspirants'] = Aspirant.objects.all()
        context['technicians'] = Technician.objects.all()
        return context


class HomeView(ActiveTabMixin, TemplateView):
    template_name = 'cathedra/home.html'
    active_tab = 'home'


lectors_list = LectorsListView.as_view()
home_view = HomeView.as_view()
