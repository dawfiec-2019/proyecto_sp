var principal = new Vue({
        el:'#principal',
    //import axios from 'axios';
        /*beforeCreate: function(){
            console.log("a")
            //console.log("as");
            this.$nextTick(function(){
                const path = 'http://localhost:8000/api/laws/';
                axios.get(path).then(function(response){
                    console.log("a")
                    this.laws = response.data;
                    //this.laws = this.laws[0]
                    //console.log(this.rate_user);
                    console.log(this.laws);
                    //console.log(this.laws[0])
                    //console.log(this.leyes.length);
                    //this.getRates();
                })
                .catch((error)=>{
                    console.log(error)
                });
            }) 
        },*/
        created: function(){
            //console.log(this.leyes)
            this.getLaws();
            this.getVotes();
            this.getComments();
            this.getUsers();

        },
        data:{
                fields:[

                {key:'name', label:'Ley'},
                //{key: 'autores', label:'Autores'},
                ],
                laws:[],
                numero_leyes:"",
                numero_votos:"",
                votos:[],
                comentarios:[],
                numero_comentarios:"",
                usuarios:[],
                numero_usuarios:"",
        },
        methods:{

            getLaws: function(){
                const path = 'http://localhost:8000/api/laws/';
                axios.get(path).then((response)=> {
                    this.laws = response.data;
                    this.numero_leyes = this.laws.length;
                    //console.log(this.rate_user);
                    //console.log(this.laws);
                    //console.log(response.data);
                    //console.log(this.numero_leyes);
                    //this.getRates();
                })
                .catch((error)=>{
                    console.log(error)
                });
            },
            getVotes: function(){

                const path = 'http://localhost:8000/api/v1.0/voto/';
                axios.get(path).then((response)=> {
                    this.votos = response.data;
                    this.numero_votos = this.votos.length;
                    //console.log(this.rate_user);
                    //console.log(this.votos);
                    //console.log(response.data);
                    //console.log(this.numero_votos);
                    //this.getRates();
                })
                .catch((error)=>{
                    console.log(error)
                });

            },
            getComments: function(){

                const path = 'http://localhost:8000/api/v1.0/comentario/';
                axios.get(path).then((response)=> {
                    this.comentarios = response.data;
                    //console.log(response.data)
                    //console.log(this.comentarios);
                    this.numero_comentarios = this.comentarios.length;
                    //console.log(this.rate_user);
                    //console.log(this.votos);
                    //console.log(response.data);
                    console.log(this.numero_comentarios.length);
                    //this.getRates();
                })
                .catch((error)=>{
                    console.log(error)
                });
            },
            getUsers: function(){

                const path = 'http://localhost:8000/api/v1.0/usuario/';
                axios.get(path).then((response)=> {
                    this.usuarios = response.data;
                    this.numero_usuarios = this.usuarios.length;
                    //console.log(this.usuarios)
                    //console.log(this.rate_user);
                    //console.log(this.votos);
                    //console.log(response.data);
                    //console.log(this.numero_votos);
                    //this.getRates();
                })
                .catch((error)=>{
                    console.log(error)
                });
            }
        }
        ,computed: {
          searchlaw: function(){
            //console.log(this.laws)
            return this.laws.filter((law)=> law.name.includes(this.name));
          }
      },
      numleyes: function(){
        return this.laws.length
      }
    });
    


    


