"""Views da aplicação abelhas."""

from django.views import generic


class AbelhaPartialView(generic.TemplateView):
    """Template para o formulário de abelha."""

    template_name = 'abelhas/partials/abelha.html'


abelha_partial_view = AbelhaPartialView.as_view()


class AbelhasPartialView(generic.TemplateView):
    """Template para listagem de abelhas."""

    template_name = 'abelhas/partials/abelhas.html'


abelhas_partial_view = AbelhasPartialView.as_view()
