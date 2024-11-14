
console.log('Page is loaded!')
const Form = document.getElementById('check-form');
const statusElement = document.getElementById('status');

Form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const url = document.getElementById('url').value;
    console.log(`URL: ${url}`);
    checkURL(url);
    event.target.reset();
});

async function checkURL(url) {
    const response = await fetch(`/check_url?url=${url}`);
    const data = await response.json ();
    console.log (data);
    console.log(`Status Code from API: ${data.status_code}`);
    if (data.status_code === 'INVALID_URL_FORMAT') {
        console.log('Invalid URL format detected');
        alert("Invalid URL format");
    } else { 
        statusElement.textContent = `Status code: ${data.status_code}`;
    }
}