var buscador = document.getElementsByClassName('searchButton');
var boton = buscador[0];
boton.type = "button";
console.log('si')
boton.addEventListener('click', function buscar(){


console.log('si');
var request = $('#busqueda').val();
request = request.toUpperCase();
var vecinos = document.getElementsByTagName('h5');
var cuadros = document.getElementsByClassName('col-md-3');

for(var i= 0; i<cuadros.length;i++){

  if(!vecinos[i].innerHTML.toUpperCase().includes(request)){
  console.log(request)
  console.log(vecinos[0].innerHTML.toUpperCase());
  cuadros[i].style.visibility = 'hidden'
  }
  else{
    cuadros[i].style.visibility = 'visible'
  }

};});		
