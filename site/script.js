function fluctuateTemperature() {
    return Math.floor(Math.random() * (25 - 20 + 1)) + 20;
}

function fluctuateHumidity() {
    return Math.floor(Math.random() * (45 - 40 + 1)) + 40;
}

function updateReadings() {
    const temperature = fluctuateTemperature();
    const humidity = fluctuateHumidity();
    document.getElementById('temperature').textContent = temperature;
    document.getElementById('humidity').textContent = humidity;
}

setInterval(updateReadings, 1000); // Update readings every second
