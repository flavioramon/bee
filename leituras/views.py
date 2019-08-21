"""Views da aplicação leituras."""

from datetime import datetime, timedelta
from django.views import generic
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Leitura


class ProcessarArquivoView(generic.TemplateView):
    """Partial contendo o formulário de envio de arquivo."""

    template_name = 'leituras/processar_arquivo.html'


processar_arquivo = ProcessarArquivoView.as_view()


class LeiturasListaView(generic.TemplateView):
    """Partial contendo a lista de leituras."""

    template_name = 'leituras/leituras_lista.html'


leituras_lista = LeiturasListaView.as_view()


def send_email(request):
    leit = Leitura.objects.values_list('bee_id', 'reading_time_local').order_by('bee_id')
    for codigo, data_hora in leit:
        for data in data_hora:
            data_temp = datetime.strftime(data, '%Y-%m-%d %H:%M:%S')
            dado = Leitura.objects.filter(bee_id=codigo).filter(reading_time_local__gt=F(data_temp) - timedelta(hours=12))
            if not dado and (dado.len() % 2) == 0:
                subject = 'alerta_bee'
                message = 'Não foram encontrados datas pares respectivos a entrada e saída.'
                from_email = 'kr_barbosa@yahoo.com.br'
                if subject and message and from_email:
                    try:
                        send_mail(subject, message, from_email, ['admin@bee.com'])
                    except BadHeaderError:
                        return HttpResponse('Cabeçalho do email é inválido.')
                    return HttpResponseRedirect(reverse('leituras:email'))
