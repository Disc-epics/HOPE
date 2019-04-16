var current_name;
var current_element;

function get_url(url) {
  let pathname = window.location.pathname.split('/');
  let num_to_splice = -3;
  if (pathname[pathname.length - 2] == 'account') {
    num_to_splice = -2;
  }
  return [... pathname.slice(0, num_to_splice), ... url ].join('/');
}

function update_center(ev) {
  current_element.classList.remove('bg-info');
  current_element = ev.target;
  current_element.classList.add('bg-info');

  // console.log(ev.target.textContent)
  current_name = ev.target.textContent.trim();
  const profile_name = document.getElementById("profile_name");
  profile_name.textContent = "Name: " + current_name;
  const remove_button = document.getElementById("remove_button");
  remove_button.href = get_url([ 'account', 'remove_client', current_name ]);

  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", get_url([ 'client_status', current_name ]), false);
  xmlHttp.send(null);
  var status = JSON.parse(xmlHttp.responseText).status;

  const profile_status = document.getElementById("profile_status");
  profile_status.textContent =
      "Status: " + (status ? "In jail" : "Not in jail");
}

window.onload = function() {
  current_element = document.getElementById('first-client');
  current_element.classList.add('bg-info');
  var evObj = document.createEvent('Events');
  evObj.initEvent('click', true, false);  // simulate the click event
  current_element.dispatchEvent(evObj);
}
