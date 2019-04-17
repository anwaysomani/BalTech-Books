var attempt = 3;

function validate() {
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;

	if(username == "Mansi" && password == "mansi123") {
		alert("Login Succesful!");
		return false;
	} else {
		alert("Seems an error!");
	}
}