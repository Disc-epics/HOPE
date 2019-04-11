function update_center(ev) {
  // console.log(ev.target.textContent)
  const profile_name = document.getElementById("profile_name");
  profile_name.textContent = "Name: " + ev.target.textContent;
  var xmlHttp = new XMLHttpRequest();
  pathname = window.location.pathname.split('/');
  let num_to_splice = -3;
  if (pathname[-1] == 'account') {
    num_to_splice = -2;
  }
  xmlHttp.open("GET",
               [
                 ... pathname.slice(0, num_to_splice), 'client_status',
                 ev.target.textContent.trim()
               ]
                   .join('/'),
               false);
  xmlHttp.send(null);
  var status = JSON.parse(xmlHttp.responseText).status;

  const profile_status = document.getElementById("profile_status");
  profile_status.textContent =
      "Status: " + (status ? "In jail" : "Not in jail");
}
