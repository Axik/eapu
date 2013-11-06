from django.views.generic import ListView

from cathedra.models import Lector


class LectorsListView(ListView):
    model = Lector
