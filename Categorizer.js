let items = [];
let num_of_questions, num_of_generations, current_question = 0, current_generation = 0;

function refresh(questionIndex, generatedIndex) {
    let item = items[questionIndex], child;
    document.getElementById("id").innerText = `Question ID: ${item.id}`;
    document.getElementById("question").innerHTML = "";
    let question = item.question.split("\n");
    console.log(question.length);
    for (let i = 0; i < question.length; i++) {
        document.getElementById("question").appendChild(document.createElement("h3")).innerText = question[i];
    } 
    document.getElementById("answer").innerHTML = "";
    let answer = item.answer.split("\n");
    for (let i = 0; i < answer.length; i++) {
        document.getElementById("answer").appendChild(document.createElement("h3")).innerText = answer[i];
    }
    document.getElementById("generated").innerHTML = "";
    let generated = item.generated[generatedIndex].split("\n");
    for (let i = 0; i < generated.length; i++) {
        document.getElementById("generated").appendChild(document.createElement("h3")).innerText = generated[i];
    }
}

function prev_question() {
    if (current_question > 0) {
        current_question--;
        current_generation = 0;
        refresh(current_question, current_generation);
    }
}

function next_question() {
    if (current_question < num_of_questions - 1) {
        current_question++;
        current_generation = 0;
        refresh(current_question, current_generation);
    }
}

function prev_generation() {
    if (current_generation > 0) {
        current_generation--;
        refresh(current_question, current_generation);
    }
    else {
        if (current_question > 0) {
            prev_question();
            current_generation = num_of_generations - 1;
            refresh(current_question, current_generation);
        }
    }
}

function next_generation() {
    if (current_generation < num_of_generations - 1) {
        current_generation++;
        refresh(current_question, current_generation);
    }
    else {
        next_question();
    }
}

document.onkeydown = function(e) {
    switch (e.key) {
        case "ArrowLeft":
            prev_generation();
            break;
        case "ArrowRight":
            next_generation();
            break
        default:
            return;
    }
}

fetch("http://localhost:8080/Questions.json")
    .then(response => response.json())
    .then(json => {
        items = json;
        num_of_questions = items.length;
        num_of_generations = items[0].generated.length;
        refresh(0, 0);
        document.getElementById("cover").remove();
    })
    .catch(error => console.error(error));
