let heading = document.querySelector("#title");

heading.addEventListener("mouseover", function() {
    heading.style.color = "green";
});


heading.addEventListener("mouseout", function() {
    heading.style.color = "black";
});