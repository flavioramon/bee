Vue.component('processarArquivo', resolve => {
  axios.get('/leituras/processar/arquivo/').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          erros: [],
          sucessos: [],
          data: {}
        }
      },
      methods: {
        converterArquivo (arquivos) {
          const arquivo = arquivos[0]
          const leitor = new FileReader()
          leitor.addEventListener('load', () => {
            this.data.arquivo = leitor.result
          })
          leitor.readAsDataURL(arquivo)
        },
        enviarArquivo () {
          this.erros = []
          this.sucessos = []
          this.loading = true
          this.Leitura.enviarArquivo(this.data).then(response => {
            this.sucessos.push(response.data)
            this.data = {}
            this.loading = false
          }).catch(response => {
            this.erros.push(response.response.data)
            this.loading = false
          })
        }
      }
    })
  })
})
