
function my_handler() {
	if ((this.readyState==4) && (this.status==200))
	{
		// retrieve the response in XML or text format
		var myXML = this.responseXML; // a DOM object
		var myText = this.responseText; // a string
		// ... do something with the response
		document.getElementById("decomposition").innerHTML = myText;
	}
	return false;
}