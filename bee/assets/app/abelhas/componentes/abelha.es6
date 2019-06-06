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
          return this.EspecieAbelha.query().then(response => {
            const reducer = (result, item) => {
              result[item.id] = item.nome
              return result
            }
            this.abelhasEspecieOptions = response.data.results.reduce(reducer, {})
          })
        },
        carregarAbelhasTipo () {
         return this.TipoAbelha.query().then(response => {
            const reducer = (result, item) => {
              result[item.id] = item.nome
              return result
            }
            this.abelhasTipoOptions = response.data.results.reduce(reducer, {})
          })
        },
        carregarAbelhasPais () {
          return this.PaisAbelha.query().then(response => {
            const reducer = (result, item) => {
              result[item.id] = item.nome
              return result
            }
            this.abelhasPaisOptions = response.data.results.reduce(reducer, {})
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
        this.loading = true
        const result = axios.spread((abelhas, tipos, paises) => {
          this.loading = false
        })

        axios.all([
          this.carregarAbelhasEspecie(),
          this.carregarAbelhasTipo(),
          this.carregarAbelhasPais()
        ]).then(result)
      }
    })
  })
})
