from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy


class MainView(RedirectView):
    ### ActiveTabmixin needed
    url = reverse_lazy('cathedra:lectors_list')


main = MainView.as_view()
