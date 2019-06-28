window.Aviso = {
  install(Vue, options) {
    const url = '/api/v1/avisos/'
    Vue.prototype.Aviso = Vue.prototype.Resource(url)
  }
}
