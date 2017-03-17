// (function app() {
    "use strict";

    var markers = [];




    function add_stop(stops) {
        var marker;
        $.each(stops, function (index, stop) {
            var stop_location = {lat: stop.lat, lng: stop.lng};
            var image = 'NEEDS USER IMAGE';
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(stop_location.lat, stop_location.lng),
                animation: google.maps.Animation.DROP,
                icon: image,
                title: 'Checked-in',
                map: map
            });
            markers.push(marker);
        })
    }

    function postCheckin(user_loc, meters) {
        $.ajax({
            url: '/api/check_ins/',   // Target Server
            method: 'POST',                                            // Request Verb
            data: {
                'lat': user_loc.lat,
                'lng': user_loc.lng,
                'radius': meters
            },                                                       // Request Params
            success: function (rsp) {                                // Success Handler
                alert(rsp);
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
            }
        });
    }

    function searchRadius(user_loc) {
        var $submit = $('#submit');
        $submit.on('click', function (event) {
            event.preventDefault();
            var $meters = $('#input_meters').val();
            postCheckin(user_loc, $meters);
        })
    }

    function get_loc() {
        navigator.geolocation.getCurrentPosition(function (position) {
            var user_loc = {lat: position.coords.latitude, lng: position.coords.longitude};
            // searchRadius(user_loc);
            postCheckin(user_loc, '500')
        });
    }

    // function getCheckin(user_loc, meters) {
    //     $.ajax({
    //         url: 'api/check_ins/',   // Target Server
    //         method: 'GET',                                            // Request Verb
    //         data: {
    //             ll: user_loc.lat + ", " + user_loc.lng,
    //             raduis_meters: meters
    //         },                                                       // Request Params
    //         success: function (rsp) {                                // Success Handler
    //             alert(rsp);
    //         },
    //         error: function (err) {                                  // Error Handler
    //             console.log(err);
    //         }
    //     });
    // }
//
// })();