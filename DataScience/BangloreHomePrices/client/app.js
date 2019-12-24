function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = document.getElementById("uiBHK");
    var bathrooms = document.getElementById("uiBathrooms");
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
		bhk: bhk.value,
		bath: bathrooms.value,
		location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "Estimated Price is: " + data.estimated_price.toString() + " Lakh";
        console.log(status);
    });
}

function onPageLoad() {
    console.log( "document loaded" );
	var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;
