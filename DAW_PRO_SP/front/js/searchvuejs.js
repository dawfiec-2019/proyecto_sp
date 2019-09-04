var urlescritores="https://firebasestorage.googleapis.com/v0/b/governus-803f2.appspot.com/o/governus-803f2-export.json?alt=media&token=6962cc81-a7ea-41d5-a802-d35aea627880";
      new Vue({
        el:'.super_container',
        created: function(){
          console.log("as");
          this.getLaws();
          
          /*this.hideAll();*/
        },
        data:{
          laws:[],
          texto:"",
        },
        methods:{
          getLaws: function(){

            this.$http.get(urlescritores).then(function(response){
              console.log(response.body.law_data.laws);
              this.laws = response.body.law_data.laws;
              this.texto= response.body.law_data.base_description;
              console.log(response.body.law_data.base_description);

              /*console.log(response.body.escritores)*/
            });
          },

          busqueda: function(){

            var request = $('#busqueda').val()
            console.log(request)
            request = request.toUpperCase();
        var arreglo_titulos = document.getElementsByClassName('display-4');
        var arreglo_columna = document.getElementsByClassName('col-md-6');
        /*arreglo_columna[0].style.visibility='hidden';*/
        console.log(arreglo_titulos[0].innerHTML.toUpperCase())

        for(var i=0;i<arreglo_columna.length;i++){
          if(!arreglo_titulos[i].innerHTML.toUpperCase().includes(request)){
            arreglo_columna[i].style.display = 'none'
          }else if(request==""){
            arreglo_columna[i].style.display = ''
          }
          else{
            arreglo_columna[i].style.visibility=''
          }

        }
        

          } 


        },
        computed: {
          searchlaw: function(){
            return this.laws.filter((law)=> law.title.includes(this.title));
          }



        }
      });
    