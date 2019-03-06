function populateAlerts() {

    const alert_json = [
        {
            name: 'John Doe',
            arrestDate: '03/05/2018',
            arrestTime: '3:26PM',
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
        {
            name: 'John Doe',
            arrestDate: '03/05/2018',
            arrestTime: '3:26PM',
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
        {
            name: 'Lorem Ipsum',
            arrestDate: '03/05/2018',
            arrestTime: '4:00PM'
        },
    ]

    // document.body.style.backgroundColor = "#AAAAAA";
    
    console.log("The function is executed!");

    const alertList = document.getElementById("alerts");

    let i = 0;
    let inner = "";
    while (i < alert_json.length) {
        inner = inner + `<li class="client_list"><div class="pallete"><ul><li class="feild">Name: ${alert_json[i].name}</li><li class="feild">Arrest Date: ${alert_json[i].arrestDate}</li><li class="feild">Time: ${alert_json[i].arrestTime}</li></ul></div></li>`;
        i++;
    }
    alertList.innerHTML = inner;
    alertList.appendChild(listElement);
}

populateAlerts();  

 