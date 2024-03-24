const api = "http://0d04-35-185-183-65.ngrok.io/get/";
const form = document.getElementById("form");
const q = document.getElementById("query");
const a = document.getElementById("answer");
const l = document.getElementById("loading");

function get(query) {
  fetch(url + query)
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      a.value = json.answer;
    })
    .then(() => {
      l.style.display = "none";
    });
}

form.addEventListener("submit",function (e) {
    e.preventDefault();
    l.style.display = "flex";
    get(q.value);
  }, false);
