/*var DATA;
var app;
var URL = "https://firebasestorage.googleapis.com/v0/b/governus-803f2.appspot.com/o/data.json?alt=media&token=8a5f6936-6306-4bfc-8b3d-a05fcd7696ae";

function load_data(){
    $.get(URL, function(data){
        DATA = data;
        app = new Vue({
            el: '#laws_app',
            data: {
                laws: DATA.law_data.laws,
                base_description: DATA.law_data.base_description
            }
        })
    });
}

load_data();
*/