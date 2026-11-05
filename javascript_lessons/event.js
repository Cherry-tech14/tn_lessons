```
let button = document.querySelector("#myButton");

button.addEventListener("click", function() {
    alert("Hello! You clicked the button.");
});
```
let heading = document.querySelector("#title")

let button = document.querySelector("#changeButton")

button.addEventListener("dblclick", function() {
    heading.textContent = "Welcome to Javascript";
});