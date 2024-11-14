console.log('Page is loaded!')
const Form = document.getElementById('form');
const status = document.getElementById('status')


Form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const temp = document.getElementById('temp').value;
    event.target.reset();
    console.log(`TEMP: ${temp}`);
    checkTemp(temp);
});

async function checkTemp(temp) {
    const response = await fetch(`/checktemp?temp=${temp}`);
    const data = await response.json();
    console.log(data.result);
    status.textContent = `${data.result}`;
    console.log(`Status Code from API: ${data.result}`);

    if (data.error) { 
        console.log(data.error); 
        alert(data.error); 
    } else { 
        document.getElementById('statusElement').textContent = `Result: ${data.result}`; 
        console.log(`Status Code from API: ${data.result}`);
    } 
}


