Vue.component('abelha', resolve => {
  axios.get('/public/app/abelhas/componentes/abelha.html').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          abelha: {
            especie: null,
            tipo: null,
            pais: null,
          },
          abelhasEspecieOptions: {},
          abelhasTipoOptions: {},
          abelhasPaisOptions: {}
        }
      },
      methods: {
        carregarAbelhasEspecie () {
          this.loading = true
          return this.EspecieAbelha.query().then(response => {
            const temp = {}
            response.data.results.forEach(e => {
              temp[e.id] = e.nome
            })
            this.abelhasEspecieOptions = temp
            this.loading = false
          })
        },
        carregarAbelhasTipo () {
          this.loading = true
         return this.TipoAbelha.query().then(response => {
            const temp = {}
            response.data.results.forEach(e => {
              temp[e.id] = e.nome
            })
            this.abelhasTipoOptions = temp
            this.loading = false
          })
        },
        carregarAbelhasPais () {
          this.loading = true
          return this.PaisAbelha.query().then(response => {
            const temp = {}
            response.data.results.forEach(e => {
              temp[e.id] = e.nome
            })
            this.abelhasPaisOptions = temp
            this.loading = false
          })
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
        this.carregarAbelhasEspecie()
        this.carregarAbelhasTipo()
        this.carregarAbelhasPais()
      }
    })
  })
})
