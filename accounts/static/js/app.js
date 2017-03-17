(function app() {
    "use strict";

    var markers = [];
    var meters = 100;

    function add_users(user_location) {
        var marker;
        $.each(user_location, function (index, user) {
            var nearby_user_loc = {lat: user.lat, lng: user.lng};
            var image = 'img/nearby-users.png';
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(nearby_user_loc.lat, nearby_user_loc.lng),
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
                alert(rsp)
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
            }
        });
    }

    function get_loc(meters) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var user_loc = {lat: position.coords.latitude, lng: position.coords.longitude};
            // searchRadius(user_loc);
            postCheckin(user_loc, meters)
        });
    }

    $('#submit').on('click', function (event) {
        event.preventDefault();
        var $meters = $('#input_meters').val();
        get_loc($meters);
    });


    function getCheckin(user_loc, meters) {
        $.ajax({
            url: 'api/check_ins/',   // Target Server
            method: 'GET',                                            // Request Verb
            data: {
                'lat': user_loc.lat,
                'lng': user_loc.lng,
                'radius': meters
            },                                                      // Request Params
            success: function (rsp) {                                // Success Handler
                var nearby_users = rsp.location;
                add_users(nearby_users);
                console.log(nearby_users)
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
            }
        });
    }

})();