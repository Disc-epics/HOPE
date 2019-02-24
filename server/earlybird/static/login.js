let username_arr = ['pandey25@purdue.edu', 'enochadu@purdue.edu'];
let password_arr = ['asdf', 'qwer'];

const login_button = document.getElementById("login-btn");

login_button.addEventListener("click", (ev) => {
    validate(ev);
});
let check_validate = false;
let link_login = document.getElementById("login-btn");
let error_msg = document.getElementById("error_msg");


function validate(ev) {
    console.log("Button has been clicked");
    let username = document.getElementById("username");
    let password = document.getElementById("password");

    /* Traversing to get the list of clients */

    let i = 0
    while (i < 2) {
        if (username_arr[i].localeCompare(username.value.trim()) === 0 &&
                password_arr[i].localeCompare(password.value.trim()) === 0) {
            /* send alert: alert(`${password_arr[i]} and ${password.value}`); */
            check_validate = true;
            break;
        }
        /* send alert: alert(`${password_arr[i]} not match ${password.value}`); */
        i++;
    }

    if (check_validate === true) {
        link_login.setAttribute('href', "./index.html");
    } else {
        alert("The Email address and password do not match");
        const paragraph = document.createElement("p");
        const text = document.createTextNode("Sorry, the password you entered is incorrect, try again!");
        paragraph.append(text);
        error_msg.append(paragraph);
        window.location.reload();        
    }
}