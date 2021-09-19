function searchFunction(){
    var input, filter, list, card, name, i, nameValue 
    input = document.getElementById("search-bar");
    filter = input.value.toLowerCase();
    list = document.querySelector('div.profile-list');
    card = list.querySelectorAll('div.card1');
    for (i = 0; i < card.length; i++) {
        name = card[i].getElementsByTagName("h5")[0];
        nameValue = name.textContent || name.innerText;
        if (nameValue.toLowerCase().indexOf(filter) > -1) {
            card[i].style.display = "";            
        } else{
            card[i].style.display = "none";
        }
    }
}
