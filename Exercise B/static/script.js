console.log('Page is loaded!')
const Form = document.getElementById('check-form');
const staus = document.getElementById('status');

Form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const url = document.getElementById('url').value;
    console.log(`URL: ${url}`);
    checkURL(url);
});

async function checkURL(url) {
    const response = await fetch(`/check_url?url=${url}`);
    const data = await response.json ();
    console.log (data);
    console.log (data.status_code);
    staus.textContent = `Status code: ${data.status_code}`;
}