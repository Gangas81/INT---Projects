console.log('Page is loaded!');
document.getElementById('status').textContent = "Testing DOM update";
document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM is fully loaded");
    document.getElementById('status').textContent = "Ready for calculation";
});


function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const dropdown = document.getElementById('dropdown').value;

    fetch(`/calc?num1=${num1}&num2=${num2}&dropdown=${dropdown}`)
        .then(response => response.json())
        .then(data => {
            console.log("Fetched result:", data.result);  // Confirm the result format
            document.getElementById('status').innerHTML = `Result: ${data.result}`;

        })
        .catch(error => console.error('Error:', error));
}
