from django.views.generic import ListView

from skd_tools.mixins import ActiveTabMixin

from cathedra.models import Lector


class LectorsListView(ActiveTabMixin, ListView):
    model = Lector
    active_tab = 'academics'


lectors_list = LectorsListView.as_view()
