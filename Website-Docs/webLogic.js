var weather = ['http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={baf131fb3ed6dea0cd72bf8aeb8762dd}']
var noResponse = "TEST_no result";

function checkButtons(){
    // Check weather
    var weather = "";
    
    if(document.getElementById("weatherYes").checked){
        displayWeather = "yes";
        weather = getWeather();
    }
    
    // Check time
    var displayClock = ""
    if(document.getElementById("clockYes").checked){
        var displayClock = "yes";
    }

    // Check event
    var displayEvents = "";
    if(document.getElementById("eventsYes").checked){
        console.log("yesEvent");
        displayEvents = "yes";
    }
    
}

function getWeather(){
    var apiCall = 'https://api.openweathermap.org/data/2.5/weather?q=Spokane&appid=baf131fb3ed6dea0cd72bf8aeb8762dd';
    var descriptionOfWeather;
    
    function weatherCallback(weatherData){
        return weatherData.weather[0].description;
    }
    
    
    return $.getJSON(apiCall, weatherCallback);
}

