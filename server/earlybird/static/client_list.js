function update_center(ev){
    //console.log(ev.target.textContent)
    const profile_name = document.getElementById("profile_name");
    profile_name.textContent = "Name: " + ev.target.textContent;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", [window.location.pathname.split('/').slice(0,-2), 'client_status', ev.target.textContent].join('/'), false);
    xmlHttp.send( null);
    var status = JSON.parse(xmlHttp.responseText).status;

    const profile_status = document.getElementById("profile_status");
    profile_status.textContent = "Status: " + (status?"In jail":"Not in jail");
}
