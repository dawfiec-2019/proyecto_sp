/*var users_data;
var laws_data;
var comments_data;
var law;
var comments = [];
var information_app, stats_app, comments_app;

function GetURLParameter(sParam){
    let sPageURL = window.location.search.substring(1);
    let sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return sParameterName[1];
        }
    }
}

function filter_data(){

    let law_id = GetURLParameter('law_id');
    law = laws_data.laws.filter(law => law.id == law_id)[0];

    comments_data.comments.forEach(function(comment){
        if(comment.lawID == law_id){
            let user = users_data.users.filter(user => user.id == comment.userID)[0];
            comments.push({comment: comment, user: user})
        }
    })

    $("title").text(law.title);

}

function auto_grow(element) {
    element.style.height = "5px";
    element.style.height = (element.scrollHeight)+"px";
}

function comment(){
    let form = $(".comment-form");
    let tmp_comment = {
        user: {"id": "U0008","photo": "avatar.png", "name": "Guest User"},
        comment: {"lawID": law.law_id, "pub_date": "Hoy", "comment": form.val()}
    }
    form.val("");
    comments_app.law_comments.push(tmp_comment);
}

var URL = "https://firebasestorage.googleapis.com/v0/b/governus-803f2.appspot.com/o/data.json?alt=media&token=8a5f6936-6306-4bfc-8b3d-a05fcd7696ae";

function load_data(){
    $.get(URL, function(data){

        users_data = data.user_data;
        laws_data = data.law_data;
        comments_data = data.comment_data;

        filter_data();

        information_app = new Vue({
            el: '#information-app',
            data: {
                laws: laws_data,
                law: law
            }
        })

        stats_app = new Vue({
            el: '#stats-app',
            data: {
                law: law
            }
        })

        comments_app = new Vue({
            el: '#comments-app',
            data: {
                law_comments : comments
            }
        })

    });
}

load_data();*/