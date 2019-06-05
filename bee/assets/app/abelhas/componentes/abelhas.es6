Vue.component('abelhas', resolve => {
  axios.get('/public/app/abelhas/componentes/abelhas.html').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          abelhas: [],
          page: 1,
          searchAbelhas: '',
          pageSizeAbelhas: 5,
          abelhasFields: [
            {key: 'codigo', label: 'Código'},
            {key: 'numero', label: 'Número'},
            {key: 'especie_data', label: 'Espécie'},
            {key: 'tipo_data', label: 'Tipo'},
            {key: 'pais_data', label: 'País'},
          ]
        }
      },
      methods: {
        carregarAbelhas (params) {
          this.loading = true
          return this.Abelha.query(params).then(response => {
            this.abelhas = response.data
            this.loading = false
          })
        },
        paginarAbelhas (page) {
          const params = {page: page, search: this.searchAbelhas, page_size: this.pageSizeAbelhas}
          return this.carregarAbelhas(params).then(() => {
            this.page = page
          })
        }
      },
      mounted () {
        this.paginarAbelhas(1)
      }
    })
  })
})
