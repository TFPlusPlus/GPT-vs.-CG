var fs = require("fs");

let data = fs.readFileSync("test.txt", "utf8");
document.getElementById("check1").checked = Int32.parse(data);
console.log(5);

function updateFile() {
    console.log(5);
    fs.writeFileSync("test.txt", Int32.parse(document.getElementById("check1").checked));
}

document.getElementById("check1").onClick = updateFile;

function load(json) {

}

fetch("Questions.json")
    .then(response => response.json())
    .then(json => load(json));