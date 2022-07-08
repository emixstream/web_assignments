//changing the onload function one could get another version of the assignment 
// <--- these simbols are used to underline the differences between the 4 implemetations



window.onload = toc4;

function toc1() {
    var items = document.getElementsByTagName("H1");
    var n = items.length;
    
    // Inizio Debug
    for (i = 0; i < n; i++)
        console.log(items[i].innerHTML);
    // Fine Debug
    
    var table = document.createElement("table");
    var thead = document.createElement("thead");
    table.appendChild(thead);
    
    var row = document.createElement("tr");
    for (i = 0; i < n; i++) {
        col = document.createElement("th");
        col.innerHTML = items[i].innerHTML;
        row.appendChild(col);
    }
    thead.appendChild(row);
    document.body.insertBefore(table, document.body.firstChild);
}

function generateAnchors(items, n) {
    for (i = 0; i < n; i++)
        items[i].id = items[i].innerHTML.replace(" ", "");
}

function toc2() {
    var items = document.getElementsByTagName("H1");
    var n = items.length;
    
    generateAnchors(items, n);                  // <---
    
    var table = document.createElement("table");
    var thead = document.createElement("thead");
    table.appendChild(thead);
    
    var row = document.createElement("tr");
    for (i = 0; i < n; i++) {
        col = document.createElement("th");
        url = document.createElement("a");      // <---
        url.href = "#" + items[i].id;           // <---
        url.innerHTML = items[i].innerHTML;     // <---
        
        col.appendChild(url);                   // <---
        row.appendChild(col);
    }
    thead.appendChild(row);
    document.body.insertBefore(table, document.body.firstChild);
}

function changeColor(item_id, color) {
    document.getElementById(item_id).style.backgroundColor = color;
}

function toc3() {
    var items = document.getElementsByTagName("H1");
    var n = items.length;
    
    generateAnchors(items, n);
    
    var table = document.createElement("table");
    var thead = document.createElement("thead");
    table.appendChild(thead);
    
    var row = document.createElement("tr");
    
    for (i = 0; i < n; i++) {
        col = document.createElement("th");
        url = document.createElement("a");
        url.href = "#" + items[i].id;
        url.innerHTML = items[i].innerHTML;
        
        url.addEventListener("mouseover", function() { changeColor(this.innerHTML.replace(" ", ""), "yellow"); });     // <---
        url.addEventListener("mouseleave", function() { changeColor(this.innerHTML.replace(" ", ""), "white"); });      // <---
        
        col.appendChild(url);
        row.appendChild(col);
    }
    thead.appendChild(row);
    document.body.insertBefore(table, document.body.firstChild);
}

function subtoc(row, h, color) {
    var items = document.getElementsByTagName(h);
    var n = items.length;
    
    generateAnchors(items, n);
    
    for (i = 0; i < n; i++) {
        col = document.createElement("th");
        url = document.createElement("a");
        url.href = "#" + items[i].id;
        url.innerHTML = items[i].innerHTML;
        
        url.addEventListener("mouseover", function() { changeColor(this.innerHTML.replace(" ", ""), color); });
        url.addEventListener("mouseleave", function() { changeColor(this.innerHTML.replace(" ", ""), "white"); });
        
        col.appendChild(url);
        row.appendChild(col);
    }
}

function toc4() {
    var table = document.createElement("table");
    var thead = document.createElement("thead");
    table.appendChild(thead);
    
    var row = document.createElement("tr");
    
    subtoc(row, "H1", "yellow");
    subtoc(row, "H2", "limegreen");
    
    thead.appendChild(row);
    document.body.insertBefore(table, document.body.firstChild);
}
