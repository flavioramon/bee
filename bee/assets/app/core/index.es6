Vue.component('index', resolve => {
  axios.get('/public/app/core/index.html').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          
        }
      }
    })
  })
})
