from django.views.generic import TemplateView, DetailView

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


class LectorDetailView(DetailView):
    model = Lector


class AspirantDetailView(DetailView):
    model = Aspirant


class TechnicianDetailView(DetailView):
    model = Technician


lectors_list = LectorsListView.as_view()
home_view = HomeView.as_view()
lector_detail = LectorDetailView.as_view()
aspirant_detail = AspirantDetailView.as_view()
technician_detail = TechnicianDetailView.as_view()
