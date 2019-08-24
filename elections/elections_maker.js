
class PoliticalParty {
    constructor(id, name, size) {
        this.id = id;
        this.name = name;
        this.size = size;
    }
}


function initUi(allParties) {
    var maxW = window.screen.width - 110;
    var maxH = window.screen.height - 300;
    var addHtml = "";
    allParties.forEach(party => {
        var top = Math.ceil(Math.random() * maxH);
        var left = Math.ceil(Math.random() * maxW);
        var div = "    <div id=\"party" + party.id + "\" class=\"mydiv\" style=\"top: " + top + "px; left: " + left + "px;\">\n" +
        "      <!-- Include a header DIV with the same name as the draggable DIV, followed by \"header\" -->\n" +
        "      <div id=\"partydivheader" + party.id + "\" class=\"mydivheader\">" + party.name + "</div>\n" +
        "      <p><i class=\"fa fa-angle-up\"></i></p>\n" +
        "      <p>" + party.size + "</p>\n" +
        "      <p><i class=\"fa fa-angle-down\"></i></p>\n" +
        "    </div>\n";

        addHtml = addHtml + div + "\n";
    });

    $('body').append(addHtml);

    allParties.forEach(party => {
        dragElement(document.getElementById("party" + party.id));
    })
}


function initParties() {
    $.ajax({
        url: "political_parties.txt"
    }).done(res => {
        let allParties = [];
        let i = 1;
        console.log(res);
        const parties = res.split('\n');
        parties.forEach(pStr => {
            pSplit = pStr.split(",");
            partyName = pSplit[0];
            partyVotes = Number(pSplit[1]);
            allParties.push(new PoliticalParty(i, partyName, partyVotes));
            i += 1;
            console.log("allParties:");
            console.log(allParties);
        });
        initUi(allParties);
    })
}


initParties();


function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    if (document.getElementById(elmnt.id + "header")) {
        // if present, the header is where you move the DIV from:
        document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
        // otherwise, move the DIV from anywhere inside the DIV:
        elmnt.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        // stop moving when mouse button is released:
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

// Make the DIV element draggable:
// dragElement(document.getElementById("mydiv"));

