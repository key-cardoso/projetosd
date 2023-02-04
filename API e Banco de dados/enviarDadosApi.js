const form = document.getElementById('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetch('http://localhost:5000/register', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(text => console.log(text))
        .catch(error => console.error(error));
});