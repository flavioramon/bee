Vue.component('abelha', resolve => {
  axios.get('/abelhas/partials/abelha/').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          abelha: {
            especie: null,
            especie_data: {},
            tipo: null,
            tipo_data: {},
            pais: null,
            pais_data: {}
          },
          /* modal especies */
          mostrarModalEspecie: false,
          especies: [],
          especieFields: [
            {key: 'id', label: 'Id'},
            {key: 'nome', label: 'Nome'}
          ],
          especieSearch: '',
          especiePageSize: 5,
          especiePage: 1,

          /* modal tipo */
          mostrarModalTipo: false,
          tipos: [],
          tipoFields: [
            {key: 'id', label: 'Id'},
            {key: 'nome', label: 'Nome'}
          ],
          tipoSearch: '',
          tipoPageSize: 5,
          tipoPage: 1,

          /* modal pais */
          mostrarModalPais: false,
          paises: [],
          paisFields: [
            {key: 'id', label: 'Id'},
            {key: 'nome', label: 'Nome'}
          ],
          paisSearch: '',
          paisPageSize: 5,
          paisPage: 1,
        }
      },
      methods: {
        /* abelhas especies */
        carregarAbelhasEspecie (params) {
          return this.EspecieAbelha.query(params).then(response => {
            this.especies = response.data
          })
        },
        paginarAbelhasEspecie(page) {
          const params = {search: this.especieSearch, page_size: this.especiePageSize, page: page}
          return this.carregarAbelhasEspecie(params).then(() => {
            this.especiePage = page
          })
        },
        abrirModalEspecie () {
          this.paginarAbelhasEspecie(1).then(() => {
            this.mostrarModalEspecie = true
          })
        },
        selecionarEspecie(items) {
          const item = items[0]
          this.abelha.especie = item.id
          this.abelha.especie_data = item
          this.mostrarModalEspecie = false
        },

        /* abelhas tipos */
        carregarAbelhasTipo (params) {
         return this.TipoAbelha.query(params).then(response => {
           this.tipos = response.data
         })
        },
        paginarAbelhasTipo (page) {
          const params = {search: this.tipoSearch, page_size: this.tipoPageSize, page: page}
          return this.carregarAbelhasTipo(params).then(() => {
            this.tipoPage = page
          })
        },
        abrirModalTipo () {
          this.paginarAbelhasTipo(1).then(() => {
            this.mostrarModalTipo = true
          })
        },
        selecionarTipo(items) {
          const item = items[0]
          this.abelha.tipo = item.id
          this.abelha.tipo_data = item
          this.mostrarModalTipo = false
        },

        /* abelhas pais */
        carregarAbelhasPais (params) {
          return this.PaisAbelha.query(params).then(response => {
            this.paises = response.data
          })
         },
         paginarAbelhasPais (page) {
           const params = {search: this.paisSearch, page_size: this.paisPageSize, page: page}
           return this.carregarAbelhasPais(params).then(() => {
             this.paisPage = page
           })
         },
         abrirModalPais () {
           this.paginarAbelhasPais(1).then(() => {
             this.mostrarModalPais = true
           })
         },
         selecionarPais(items) {
           const item = items[0]
           this.abelha.pais = item.id
           this.abelha.pais_data = item
           this.mostrarModalPais = false
         },

        cadastrarAbelha () {
          this.loading = true
          this.Abelha.save(this.abelha).then(() => {
            this.loading = false
            this.$router.push('/')
          })
        }
      },
      mounted () {
      }
    })
  })
})
