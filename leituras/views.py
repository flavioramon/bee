"""Views da aplicação leituras."""

from django.views import generic


class ProcessarArquivoView(generic.TemplateView):
    """Partial contendo o formulário de envio de arquivo."""

    template_name = 'leituras/processar_arquivo.html'


processar_arquivo = ProcessarArquivoView.as_view()


class LeiturasListaView(generic.TemplateView):
    """Partial contendo a lista de leituras."""

    template_name = 'leituras/leituras_lista.html'


leituras_lista = LeiturasListaView.as_view()
