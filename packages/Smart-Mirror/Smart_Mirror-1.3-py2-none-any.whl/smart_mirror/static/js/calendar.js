var day = new Date().getDate();
var month = new Date().getMonth();
var year = new Date().getFullYear();


function displayCalendar(){
    var htmlContent ="";
    var FebNumberOfDays ="";
    var counter = 1;
    
    if(month>11)
    {
        month = 0;
        year += 1;
    }
    else if(month<0)
    {
        month = 11;
        year -= 1;
    }
    console.log(year + "-" + month);
    var dateNow = new Date(year,month);
    
    var nextMonth = month+1; //+1; //Used to match up the current month with the correct start date.
    // if(nextMonth > 11)
    // {
    //     nextMonth = 0;
    //     year += 1
    // }

    // alert(month);
    var prevMonth = month -1;
    


    //Determing if February (28,or 29)  
    if (month == 1){
    if ( (year%100!=0) && (year%4==0) || (year%400==0)){
        FebNumberOfDays = 29;
    }else{
        FebNumberOfDays = 28;
    }
    }


    // names of months and week days.
    var monthNames = ["January","February","March","April","May","June","July","August","September","October","November", "December"];
    var dayNames = ["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday", "Saturday"];
    var dayNamesShort = ["Sun","Mon","Tue","Wed","Thr","Fri", "Sat"];
    var dayPerMonth = ["31", ""+FebNumberOfDays+"","31","30","31","30","31","31","30","31","30","31"]


    // days in previous month and next one , and day of week.
    var nextDate = new Date(nextMonth +' 1 ,'+year);
    var weekdays= nextDate.getDay();
    var weekdays2 = weekdays
    var numOfDays = dayPerMonth[month];
        



    // this leave a white space for days of pervious month.
    while (weekdays>0){
    htmlContent += "<td class='monthPre'></td>";

    // used in next loop.
        weekdays--;
    }

    var todayDay = "";
    // loop to build the calander body.
    while (counter <= numOfDays){

        // When to start new line.
    if (weekdays2 > 6){
        weekdays2 = 0;
        htmlContent += "</tr><tr>";
    }



    // if counter is current day.
    // highlight current day using the CSS defined in header.
    if (counter == day){
        todayDay = weekdays2;
        htmlContent +="<td class='dayNow'  onMouseOver='this.style.background=\"#4ecdc4\"; this.style.color=\"#FFFFFF\"' "+
        "onMouseOut='this.style.background=\"#f5f5f5\"; this.style.color=\"#555555\"'>"+counter+"</td>";
    }else{
        htmlContent +="<td class='monthNow' onMouseOver='this.style.background=\"#4ecdc4\"'"+
        " onMouseOut='this.style.background=\"#f5f5f5\"'>"+counter+"</td>";    

    }

    weekdays2++;
    counter++;
    }

    var calendarHead = "<div class='calendarHead flex-container'>" + dayNames[todayDay] + "<br><div id='todayDate'>" + day + "</div></div>"


    // building the calendar html body.
    var calendarBody = "<table style='border-spacing: 0; border-width: 0; padding: 0; border-width: 0;' class='fullCalendar'><tr><td style='padding-right: 0px;'>" + calendarHead + "</td><td style='padding-left: 0px;'> <table style='border-spacing: 0; border-width: 0; padding: 0; border-width: 0;' class='calendar'> <tr class='monthNow'><td><button onclick='month = " + prevMonth + "; displayCalendar();'><</button></td><th colspan='5'>"
    +monthNames[month]+" "+ year +"</th><td><button onclick='month = " + nextMonth + "; displayCalendar();'>></button></td></tr>";
    calendarBody +="<tr class='dayNames'>";
    dayNamesShort.forEach(function(dayName){
        calendarBody += "<td>" + dayName + "</td>";
    });
    calendarBody += "</tr><tr>";
    calendarBody += htmlContent;
    calendarBody += "</tr></table>    </td></tr></table>";
    // set the content of div .
    document.getElementById("calendar").innerHTML=calendarBody;
}