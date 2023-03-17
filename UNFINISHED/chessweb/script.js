function autoRefresh() {
    window.location = window.location.href;
}
setInterval('autoRefresh()', 5000);

function sendData() {
    var form = document.getElementById("move");

    form.addEventListener("submit", function(event) {
    event.preventDefault();

    var move = document.getElementById("move").value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "Main");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        // Update the page with the response from the server
        var response = xhr.responseText;
        document.getElementById("move").textContent = response + "'s move";
        }
    };
    xhr.send("move=" + encodeURIComponent(move));
    });
}