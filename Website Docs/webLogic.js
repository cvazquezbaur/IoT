var showWeather;
var showClock;
var showEvents;
var eventId;
var popular;
var events = ['https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId'];
var weather = ['http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={baf131fb3ed6dea0cd72bf8aeb8762dd}']

function getTimes(){
    var d = getDate();
    var n = d.getTime();
    print("test");
}

function getDate(){
    var d = new Date();
}

if(document.getElementById(weatherYes).checked){
    //access weather api
}else{

}

if(document.getElementById(clockYes).checked){
    getTimes();
}else{

}

if(document.getElementById(calendarYes).checked){
    //access calendarr api
}else{
    
}


function getEvents() {
    var request = new XMLHttpRequest();


    request.open('GET', eventId[random1], false);
    request.setRequestHeader();
    request.send();

    let answer = JSON.parse(request.responseText);
    eventId = answer.event;
   // pop1 = answer.arr1.popularity;
    console.log(answer.event + " TEST");

}

function getWeather(){
    var request = new XMLHttpRequest();
    
  //  import requests
    response = requests.get(
        url='https://www.googleapis.com/calendar/v3/users/me/calendarList',
        headers={'Authorization': 'Bearer ACCESS_TOKEN'},
    )
    response.raise_for_status()
    calendars = response.json().get('items')

    temp = sense.get_temperature()
}


// page_token = None
// while True:
//   events = service.events().list(calendarId='primary', pageToken=page_token).execute()
//   for event in events['items']:
//     print event['summary']
//   page_token = events.get('nextPageToken')
//   if not page_token:
//     break

//this will return events on the specified calendar
