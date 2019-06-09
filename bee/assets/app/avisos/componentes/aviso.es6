Vue.component('aviso', resolve => {
  axios.get('/avisos/partials/aviso/').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          loading: false,
          aviso: {}
        }
      },
      methods: {
        cadastrarAviso () {
          this.loading = true
          this.Aviso.save(this.aviso).then(() => {
            this.loading = false
            this.$router.push('/')
          })
        }
      }
    })
  })
})
