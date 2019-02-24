let username_arr = ['pandey25@purdue.edu', 'enochadu@purdue.edu'];
let password_arr = ['asdf', 'qwer'];

const login_button = document.getElementById("login-btn");

login_button.addEventListener("click", (ev) => {
    validate(ev);
});
let check_validate = false;
const link_login = document.getElementById("login-btn");
const error_para = document.getElementById("error_msg");

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
        // const paragraph = document.createElement("p");
        // const text = document.createTextNode("Sorry, the password you entered is incorrect, try again!");
        // paragraph.innerHTML(text);
        error_msg.textContent = "Sorry, the email and password combination is incorrect, try again!";
        // alert("The Email address and password do not match");       
    }
}