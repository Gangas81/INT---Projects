
console.log('Page is loaded!')
    // Define all constants at the beginning
const Clock = document.getElementById('Showtime');

Clock.addEventListener('click', () => {
    console.log('button clicked'); //reference to check if the button is clickable
    ShowTime();
});

// The ShowTime function performs the following steps:
// Fetches data from the /get_time route.
// Parses the response as JSON.
// Logs the data to the console.
// Updates the inner HTML of an element with the ID Clock to display the current time.
// we use async and wait because JS will keep excuting the code before response will arrive, so we wait for response then continue.
async function ShowTime() {
    const time = await fetch ('/get_time');
    const data = await time.json ();
    console.log (data);
    Clock.innerHTML = data.time; //innerhtml will change the text inside the button
    
}