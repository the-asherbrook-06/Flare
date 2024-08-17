var inputField = document.querySelector("#content .top .search .input");
var submitBtn = document.querySelector("#content .top .search .button");

inputField.addEventListener('focus', () => {
    inputField.classList.toggle('glow');
    submitBtn.classList.toggle('glow');
});

inputField.addEventListener('blur', () => {
    inputField.classList.remove('glow');
    submitBtn.classList.remove('glow');
});
