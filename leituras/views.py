"""Views da aplicação leituras."""

from django.views import generic


class ProcessarArquivoView(generic.TemplateView):
    """Partial contendo o formulário de envio de arquivo."""

    template_name = 'leituras/processar_arquivo.html'


processar_arquivo = ProcessarArquivoView.as_view()
