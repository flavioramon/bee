window.User = {
  install(Vue, options) {
    const url = '/api/v1/usuarios/'
    Vue.prototype.User = Vue.prototype.Resource(url)
  }
}

window.Abelha = {
  install (Vue, options) {
    const url = '/api/v1/abelhas/'
    Vue.prototype.Abelha = Vue.prototype.Resource(url)
  }
}

window.EspecieAbelha = {
  install (Vue, options) {
    const url = '/api/v1/abelhas-especie/'
    Vue.prototype.EspecieAbelha = Vue.prototype.Resource(url)
  }
}

window.TipoAbelha = {
  install (Vue, options) {
    const url = '/api/v1/abelhas-tipo/'
    Vue.prototype.TipoAbelha = Vue.prototype.Resource(url)
  }
}

window.PaisAbelha = {
  install (Vue, options) {
    const url = '/api/v1/abelhas-pais/'
    Vue.prototype.PaisAbelha = Vue.prototype.Resource(url)
  }
}