document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript has loaded');

// ---------------------
// BUTTON
// ---------------------

  const button = document.querySelector("#button");
  const handleButtonClick = function(){
    const resultParagraph = document.querySelector("#button-result");
    resultParagraph.textContent = "That button was clicked right into next week";
  };
  button.addEventListener("click", handleButtonClick);

// ---------------------
// INPUT
// ---------------------

const textInput = document.querySelector("#input");
  // 1. Get value from the input
  // 2. Update the paragraph text
  const handleInput = function(event) {
    const resultParagraph = document.querySelector("#input-result");
    resultParagraph.textContent = "You typed " + event.target.value;
  };
  
  textInput.addEventListener("input", handleInput);


// ---------------------
// SELECT
// ---------------------

const select = document.querySelector("#select");

const handleSelectChange = function(event) {
  const resultParagraph = document.querySelector("#select-result");
  resultParagraph.textContent = "You chose " + event.target.value;
};

select.addEventListener("change", handleSelectChange);


// ---------------------
// FORM
// ---------------------

const form = document.querySelector("#form");

const handleFormSubmit = function(event) {
  event.preventDefault();
  const resultParagraph = document.querySelector("#form-result");
  resultParagraph.textContent =
  `Your name:
  ${event.target.first_name.value}
  ${event.target.last_name.value}`
};

form.addEventListener("submit", handleFormSubmit);
});

