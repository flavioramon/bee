Vue.component('leiturasLista', resolve => {
  axios.get('/leituras/lista/').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          leituras: [],
          leiturasFields: [
            {key: 'id', label: 'ID'},
            {key: 'reading_time_local', label: 'Tempo de leitura'},
            {key: 'bee_id', label: 'ID da abelha'},
            {key: 'antenna', label: 'Antena'},
            {key: 'pc_id', label: 'PC ID'},
            {key: 'ambient_temperature', label: 'Temperatura'}
          ],
          leiturasPage: 1,
          leiturasPageSize: 5,
          leiturasSearch: ''
        }
      },
      methods: {
        carregarLeituras (params) {
          return this.Leitura.query(params).then(response => {
            this.leituras = response.data
          })
        },
        paginarLeituras (page) {
          this.loading = true
          const params = {page: page, page_size: this.leiturasPageSize, search: this.leiturasSearch}
          return this.carregarLeituras(params).then(() => {
            this.leiturasPage = page
            this.loading = false
          })
        }
      },
      mounted () {
        this.paginarLeituras(1)
      }
    })
  })
})
