const template = `
    <div class="col-sm-4 caseworker">
        <p class="text-center"><strong>Case Worker 1 </strong></p><br>
        <a href="#info6" data-toggle="collapse">
            <center>
                <img src="../static/images/CaseworkerPicture.jpeg" class="img-circle person" alt="Random Name" width="255" height="255" style="width: 300px;">
            </center>
            <br>
        </a>

        <div id="info6" class="collapse text-center">
            <p>Client List</p>
            <p>Remove Case Worker</p>
        </div>
    </div>
`;

test = document.getElementById("add_template")
console.log(test)

for(var i =0 ;i < 6; i= i + 1){
    span = document.createElement('span')
    span.innerHTML = template
    test.append(span)
}

