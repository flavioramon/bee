Vue.component('avisosLista', resolve => {
  axios.get('/avisos/lista/').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          avisos: [],
          page: 1,
          searchAvisos: '',
          pageSizeAvisos: 5,
          avisosFields: [
            {key: 'codigo', label: 'Código'},
            {key: 'descricao', label: 'Descrição'}
          ]
        }
      },
      methods: {
        carregarAvisos (params) {
          this.loading = true
          return this.Aviso.query(params).then(response => {
            this.avisos = response.data
            this.loading = false
          })
        },
        paginarAvisos (page) {
          const params = {page: page, search: this.searchAvisos, page_size: this.pageSizeAvisos}
          return this.carregarAvisos(params).then(() => {
            this.page = page
          })
        }
      },
      mounted () {
        this.paginarAvisos(1)
      }
    })
  })
})
