var showWeather;
var showClock;
var showEvents;
var eventId;
var popular;
//var events = ['https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId'];
var weather = ['http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={baf131fb3ed6dea0cd72bf8aeb8762dd}']
var noResponse = "TEST_no result";

function checkWeatherButton(){
    if(document.getElementById("weatherYes").checked){
        getWeather();
    }else{
        console.log("TEST_no result");
    }
}


function getWeather(){
    console.log("In getWeather()");

    var apiCall = 'https://api.openweathermap.org/data/2.5/weather?q=Spokane&appid=baf131fb3ed6dea0cd72bf8aeb8762dd';

    $.getJSON(apiCall, weatherCallback);
    
    function weatherCallback(weatherData){
            console.log(weatherData.weather[0].description);
            var descriptionOfWeather = weatherData.weather[0].description
    }
    console.log(descriptionOfWeather);


}


// function getTimes(){
//     var d = getDate();
//     var n = d.getTime();
//     print("test");
// }

// function getDate(){
//     var d = new Date();
// }



// if(document.getElementById(clockYes).checked){
//     getTimes();
// }else{

// }

// if(document.getElementById(calendarYes).checked){
//     //access calendarr api
// }else{
    
// }


// function getEvents() {
//     var request = new XMLHttpRequest();

//     request.open('GET', eventId[random1], false);
//     request.setRequestHeader();
//     request.send();

//     let answer = JSON.parse(request.responseText);
//     eventId = answer.event;
//    // pop1 = answer.arr1.popularity;
//     console.log(answer.event + " TEST");

// }

   


// page_token = None
// while True:
//   events = service.events().list(calendarId='primary', pageToken=page_token).execute()
//   for event in events['items']:
//     print event['summary']
//   page_token = events.get('nextPageToken')
//   if not page_token:
//     break

//this will return events on the specified calendar

// var apiCall = api.openweathermap.org/data/2.5/weather?q=Spokane&Appid=baf131fb3ed6dea0cd72bf8aeb8762dd;

// $.JSON(apiCall, weatherCallback);

// function weatherCallback(weatherData){
//     console.log(weatherData);

// }
// //  import requests
// response = requests.get(
//     url='https://www.googleapis.com/calendar/v3/users/me/calendarList',
//     headers={'Authorization': 'Bearer ACCESS_TOKEN'},
// )
// response.raise_for_status()
// calendars = response.json().get('items')

// temp = sense.get_temperature()
// }
