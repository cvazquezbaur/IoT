<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
<?php
echo "hii";
  if (isset($_POST['submit'])){
    $time_presence = boolval($_POST['clock']);
    $weather_presence = boolval($_POST['weather']);
    $event_presence = boolval($_POST['event']);
    
    exec("python /usr/local/home/pi/final/matrix-code/bindings/python/c3/SmartFrame.py '$time_presence' '$weather_presence' '$event_presence'");
?>
<!DOCTYPE html>
<html>
<script type="text/javascript">
function validateForm(){
    // Check weather
    var weather = "";
    
    if(document.myform.weatherYes.checked){
        displayWeather = "yes";
    }
    
    // Check time
    var displayClock = ""
    if(document.myform.clockYes.checked){
        var displayClock = "yes";
    }

    // Check event
    var displayEvents = "";
    if(document.myform.eventsYes.checked){
        console.log("yesEvent");
        displayEvents = "yes";
    }
    return true;
}

</script>
<head>
<title>C3</title>
</head>

<h1>C3 LED Matrix Smart Clock</h1>
<body>
	<form name="myform" onsubmit="return validateForm(this);" action = "website.php" method = "post">
	    <p>Show Clock:</p>
	      <input type="radio" id="clockYes" name="clock" value="clockYes">
	      <label for="clockYes">Yes</label><br>
	      <input type="radio" id="clockNo" name="clock" value="">
	      <label for="clockNo">No</label><br>
	 
	    <p>Show Weather:</p>
	      <input type="radio" id="weatherYes" name="weather" value="weather">
	      <label for="weatherYes">Yes</label><br>
	      <input type="radio" id="weatherNo" name="weather" value="">
	      <label for="weatherNo">No</label><br>
	    
	    <p>Show Calendar Events:</p>
	      <input type="radio" id="eventsYes" name="calendar" value="calendar">
	      <label for="calendarYes">Yes</label><br>
	      <input type="radio" id="eventsNo" name="calendar" value="">
	      <label for="calendarNo">No</label><br>

	      <input name = "submit" type="submit" value="Submit Preferences">
    	</form>
</body>

<style>

@import url('https://fonts.googleapis.com/css?family=Barlow+Semi+Condensed&display=swap');    
    * {
        font-family: 'Barlow Semi Condensed', sans-serif;    }
    p{
        font-size: 30px;   
    }
    label{
        font-size: 20px;
    }
    h1{
        background-color: lightgrey;
        width: 350px;
         border: 7px solid black;
    }
</style>

<body bgcolor="#E0E0E0"></body>
</html>
