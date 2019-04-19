function validate() {
	// Extract user information from form(by Id element)
	var passcode = document.getElementById("passcode").value;

	// Actual function to validate if user found guilty
	if(passcode == "daily") {
		// Action to perform if successful
		alert("Login Succesful!");
		window.location = "pages/personalinfo.html";
		return false;
	} else {
		// Action to perform if not successful
		alert("Seems an error!");
	}
}