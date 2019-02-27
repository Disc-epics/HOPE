let names = ["John Doe", 
"Eugenia Sweeting",
"Grant Muscarella",
"Kristle Rahimi",
"Bo Cockett",
"Valentina Rentschler",
"Chester Vowels",
"Idella Wagar",
"Marva Farish",
"Desire Westbrooks",
"Myrta Pottorff",
"Francis Culotta",
"Lin Roff",
"Laure Sherk",
"Lorilee Temples",
"Priscila Kari",
"Dori Loffredo",
"Edmond Summerfield",
"Inga Sheetz",
"Talia Elmore"];

function populate_list(){
    homeless_list = document.getElementById("final_list");

    for(var i in names){
        const item = document.createElement("li");
        item.classList.add("list_name");
        item.textContent= names[i];

        item.addEventListener("click", (ev) => {
            update_center(ev);
        });

        homeless_list.appendChild(item)
    }
}

function update_center(ev){
    //console.log(ev.target.textContent)
    const profile_name = document.getElementById("profile_name");
    profile_name.textContent = "Name: " + ev.target.textContent;
}

populate_list();