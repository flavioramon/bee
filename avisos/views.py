"""Views da aplicação avisos."""

from django.views import generic


class AvisosListaView(generic.TemplateView):
    """Template para o formulário de aviso."""

    template_name = 'avisos/avisos_lista.html'


aviso_lista_view = AvisosListaView.as_view()
