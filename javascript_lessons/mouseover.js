```
let heading = document.querySelector("#title");

heading.addEventListener("mouseover", function() {
    heading.style.color = "green";
});


heading.addEventListener("mouseout", function() {
    heading.style.color = "black";
});
```

let button = document.querySelector("#myButton");

button.addEventListener("mouseover", function() {
    button.style.backgroundColor = "green";
});

button.addEventListener("mouseout", function() {
    button.style.backgroundColor = "yellow";
});