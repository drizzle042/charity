// initialize AOS
AOS.init();
// universal variables
var menu = document.getElementById('menu-icon');
var dropdown = document.querySelector('#dropdown');
var closeImg = document.querySelector('#close');
var language1 = document.querySelector('#language1');
var language2 = document.querySelector('#language2');
var form = document.querySelector('.language-form');
var cancel = document.querySelector('button.cancel');

// click event for menu icon
menu.addEventListener("click", function(e){
    e.currentTarget.style.display = 'none';
    dropdown.style.display = 'block';
});
// click event for menu dropdown
closeImg.addEventListener("click", function(e){
    dropdown.style.display ='none';
    menu.style.display = 'block';
});
// click event for language selection
language1.addEventListener("click", function(e){
    form.style.display = 'block';
    dropdown.style.display ='none';
    menu.style.display = 'block';
});
language2.addEventListener("click", function(e){
    form.style.display = 'block';
});
cancel.addEventListener("click", function(e){
    form.style.display = 'none';
});