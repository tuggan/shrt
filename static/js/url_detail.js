url = window.location.origin;
endpoint = 'api/';
dateOptions = {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', 
    hour: 'numeric', minute: 'numeric', second: 'numeric'
}

function getID(element = 'url_id') {
   e = document.getElementById(element);
    if (e != null) {
        return e.textContent;
    } else {
        return;
    }
};


async function getHistory(url = '', id = 0, fn) {
    fetch(`${url}/${endpoint}log/?url=${id}`, {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }})
        .then(response => response.json())
        .then(data => fn(data));
};


function appendHistory(data) {
    var content = document.getElementById("content");

    // Create history text
    h = document.createElement("h1");
    h.textContent = "History";
    content.appendChild(h);

    // Create table and header
    var row_data = [["Country", "country_code"], ["Date", "time"]];
    var table = document.createElement("table");
    var tr = document.createElement("tr");

    // For column create table heder
    for (rd of row_data) {
        var th = document.createElement("th");
        th.textContent = rd[0];
        tr.appendChild(th);
    }
    table.appendChild(tr);


    // For each result in history fetch
    for (const h of data.results) {
        var tr = document.createElement("tr");
        for (var rd of row_data) {
            var td = document.createElement("td");
            if (h[rd[1]] === null) {
                text = "None";
            } else if (rd[1] == "time") {
                text = new Date(h[rd[1]]).toLocaleDateString(undefined, dateOptions);
            } else {
                text = h[rd[1]];
            }
            td.textContent = text
            tr.appendChild(td);
        };
        table.appendChild(tr);
    };
    content.appendChild(table);
};


documentReady(function () {
    id = getID()
    if (id) {
        getHistory(url, id, appendHistory);
    }
});

