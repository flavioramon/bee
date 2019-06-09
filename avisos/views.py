"""Views da aplicação avisos."""

from django.views import generic


class AvisoPartialView(generic.TemplateView):
    """Template para o formulário de aviso."""

    template_name = 'avisos/partials/aviso.html'


aviso_partial_view = AvisoPartialView.as_view()


class AvisosPartialView(generic.TemplateView):
    """Template para listagem de avisos."""

    template_name = 'avisos/partials/avisos.html'


avisos_partial_view = AvisosPartialView.as_view()
