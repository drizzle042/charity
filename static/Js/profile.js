// universal variables
followButton = document.getElementById("follow-button");
emailEntry = document.querySelector("section.followers-email-card");
cancelButton = document.getElementById("cancel");

// follow button action
followButton.addEventListener("click", function(e){
    emailEntry.style.display = 'block';
});

// cancel button action
cancelButton.addEventListener("click", function(e){
    emailEntry.style.display = 'none';
});