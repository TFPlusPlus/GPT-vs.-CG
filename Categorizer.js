let QUESTIONS = [], CATEGORIES = [], CATEGORIES_INDICES = [], data = [], checked = [];
let num_of_questions, num_of_generations, num_of_categories, current_question = 0, current_generation = 0, current_category = 0;

function refresh() {
    let item = QUESTIONS[current_question];
    document.getElementById("id").innerText = `Question: ${current_question + 1}/${num_of_questions} (ID: ${item.id})`;
    document.getElementById("question").innerHTML = "";
    let question = item.question.split("\n");
    for (let i = 0; i < question.length; i++) {
        document.getElementById("question").appendChild(document.createElement("h3")).innerText = question[i];
    }
    document.getElementById("answer").innerHTML = "";
    let answer = item.answer.split("\n");
    for (let i = 0; i < answer.length; i++) {
        document.getElementById("answer").appendChild(document.createElement("h3")).innerText = answer[i];
    }
    document.getElementById("generated").innerHTML = "";
    let generated = item.generated[current_generation].split("\n");
    for (let i = 0; i < generated.length; i++) {
        document.getElementById("generated").appendChild(document.createElement("h3")).innerText = generated[i];
    }
    document.getElementById("generated-index").innerText = `Generation: ${current_generation + 1}/${num_of_generations}`;
    document.getElementById("category").innerText = `Category: ${current_category + 1}/${num_of_categories} (${CATEGORIES[current_category].category})`;
    document.getElementById("options").innerHTML = "";
    let options = CATEGORIES[current_category].options, input, label;
    for (let i = 0; i < options.length; i++) {
        input = document.createElement("input");
        input.type = "checkbox";
        input.id = `checkbox${i}`;
        label = document.createElement("label");
        label.appendChild(input);
        label.innerHTML += options[i];
        document.getElementById("options").appendChild(document.createElement("div")).appendChild(label);
        if (data[current_question][CATEGORIES_INDICES[current_category] + i] == 1) {
            document.getElementById(`checkbox${i}`).checked = true;
            checked.push(i);
        }
    }
}

function prev_question() {
    if (current_question > 0) {
        current_question--;
        current_generation = 0;
        current_category = 0;
        refresh();
    }
}

function next_question() {
    if (current_question < num_of_questions - 1) {
        current_question++;
        current_generation = 0;
        current_category = 0;
        refresh();
    }
}

function prev_generation() {
    if (current_generation > 0) {
        current_generation--;
        refresh();
    }
}

function next_generation() {
    if (current_generation < num_of_generations - 1) {
        current_generation++;
        refresh();
    }
}

function prev_category() {
    update_data();
    if (current_category > 0) {
        current_category--;
    }
    else if (current_question > 0) {
        current_category = num_of_categories - 1;
        current_question--;
        current_generation = num_of_generations - 1;
    }
    if (num_of_categories - num_of_generations <= current_category) {
        current_generation = current_category + num_of_generations - num_of_categories;
    }
    refresh();
}

function next_category() {
    update_data();
    if (current_category < num_of_categories - 1) {
        current_category++;
    }
    else if (current_question < num_of_questions - 1) {
        current_category = 0;
        current_question++;
        current_generation = 0;
    }
    if (num_of_categories - num_of_generations <= current_category) {
        current_generation = current_category + num_of_generations - num_of_categories;
    }
    refresh();
}

function prepare_list() {
    let question_button, question_box, item, question;
    for (let i = 0; i < QUESTIONS.length; i++) {
        item = QUESTIONS[i];
        question_button = document.createElement("button");
        question_button.innerText = `Jump to Question ${item.id}`;
        question_button.onclick = function() {
            current_question = i;
            current_generation = 0;
            current_category = 0;
            refresh();
            hide_list();
        };
        question_box = document.createElement("div");
        question_box.className = "box";
        question = item.question.split("\n");
        for (let i = 0; i < question.length; i++) {
            question_box.appendChild(document.createElement("h3")).innerText = question[i];
        }
        document.getElementById("list").appendChild(question_button);
        document.getElementById("list").appendChild(question_box);
    }
}

function hide_list() {
    document.getElementById("cover").style.display = "none";
    document.getElementById("main").style.display = "block";
}

function show_list() {
    document.getElementById("cover").style.display = "block";
    document.getElementById("main").style.display = "none";
}

function update_data() {
    for (let i = 0; i < CATEGORIES_INDICES[current_category + 1] - CATEGORIES_INDICES[current_category]; i++) {
        if (checked.includes(i)) {
            data[current_question][CATEGORIES_INDICES[current_category] + i] = 1;
        }
        else {
            data[current_question][CATEGORIES_INDICES[current_category] + i] = 0;
        }
    }
    checked = [];
}

function save() {

}

function load() {
    
}

document.onkeydown = function(e) {
    switch (e.key) {
        case "ArrowLeft":
            prev_category();
            break;
        case "ArrowRight":
            next_category();
            break
        default:
            break;
    }
    if (e.key >= "0" && e.key <= "9") {
        let checkbox = document.getElementById(`checkbox${e.key - "0"}`);
        if (checkbox) {
            checkbox.checked = !checkbox.checked;
            checked.push(e.key - "0");
        }
    }
}

// fetch("http://localhost:8080/Questions.json")
fetch("Questions.json")
    .then(response => response.json())
    .then(questions_json => {
        fetch("Categories.json")
            .then(response => response.json())
            .then(categories_json => {
                QUESTIONS = questions_json;
                CATEGORIES = categories_json;
                let current_index = 0, i = 0;
                for (i = 0; i < CATEGORIES.length; i++) {
                    CATEGORIES_INDICES[i] = current_index;
                    current_index += CATEGORIES[i].options.length;
                }
                CATEGORIES_INDICES[i] = current_index;
                for (let i = 0; i < QUESTIONS.length; i++) {
                    data.push(Array(current_index).fill(0));
                }
                num_of_questions = QUESTIONS.length;
                num_of_generations = QUESTIONS[0].generated.length;
                num_of_categories = CATEGORIES.length;
                prepare_list();
                refresh(0, 0);
                hide_list();
                document.getElementById("loading").remove();
            })
            .catch(error => console.error(error));
    })
    .catch(error => console.error(error));
