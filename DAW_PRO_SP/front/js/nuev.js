new Vue({
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

        },
        data:{
            fields:[

                {key:'id', label:'ID'},
                //{key: 'autores', label:'Autores'},
                ],
                laws:[]
        },
        methods:{

            getLaws: function(){
                const path = 'http://localhost:8000/api/laws/';
                axios.get(path).then((response)=> {
                    this.laws = response.data;
                    //console.log(this.rate_user);
                    console.log(this.laws);
                    console.log(response.data);
                    //this.getRates();
                })
                .catch((error)=>{
                    console.log(error)
                });
            }
        }
        ,computed: {
          searchlaw: function(){
            console.log(this.laws)
            return this.laws.filter((law)=> law.name.includes(this.name));
          }
      }
    });