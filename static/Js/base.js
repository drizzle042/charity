// initialize AOS
AOS.init();
// universal variables
var menu = document.getElementById('menu-icon');
var dropdown = document.querySelector('#dropdown');
var closeImg = document.querySelector('#close');
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