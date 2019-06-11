window.User = {
  install(Vue, options) {
    const url = '/api/v1/usuarios/'
    Vue.prototype.User = Vue.prototype.Resource(url)
  }
}

window.Leitura = {
  install(Vue, options) {
    const url = '/api/v1/leituras/'
    Vue.prototype.Leitura = Vue.prototype.Resource(url, {
      enviarArquivo (data) {
        return axios.post(`${url}processar_arquivo/`, data)
      }
    })
  }
}
