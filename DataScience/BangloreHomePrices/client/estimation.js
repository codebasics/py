function estimate() {
	console.log("Button clicked");
	
	// var sqft = document.getElementById("Squareft");
	// console.log("Sqft:",sqft.value);
	
    // var url = "http://127.0.0.1:5000/predict_home_price";
    // $.post(url, {
    //     total_sqft: parseFloat(sqft.value),
	// 	bhk: 2,
	// 	bath: 2,
	// 	location: "Electronic City Phase II"
    // },function(data, status) {
    //     console.log(data);
    //     console.log(status);
    // });
	
  /* var x = document.getElementById("price");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  } */
}

function onPageLoad() {
    console.log( "document loaded" );
	// var url = "http://127.0.0.1:5000/get_location_names";
    // $.get(url,function(data, status) {
    //     console.log("got response for get_location_names request");
    //     if(data) {
    //         var locations = data.locations;
    //         var uiLocations = document.getElementById("uiLocations");
    //         $('#uiLocations').empty();
    //         for(var i in locations) {
    //             var opt = new Option(locations[i]);
    //             $('#uiLocations').append(opt);
    //         }
    //     }
    // });
}

window.onload = onPageLoad;

// $(document).ready(function() {
//     if(pageInitialized) return;
//     console.log( "document loaded" );
// 	var url = "http://127.0.0.1:5000/get_location_names";
//     $.get(url,function(data, status) {
//         console.log("got response for get_location_names request");
//         if(data) {
//             var locations = data.locations;
//             var uiLocations = document.getElementById("uiLocations");
//             $('#uiLocations').empty();
//             for(var i in locations) {
//                 var opt = new Option(locations[i]);
//                 $('#uiLocations').append(opt);
//             }
//             pageInitialized = true;
//         }
//     });		
// });