(function app() {
    "use strict";

    var markers = [];
    var meters = 100;

    function add_users(nearby_users) {
        var map;
        var marker;
        console.log(nearby_users);
        $.each(nearby_users, function (index, user) {
            console.log(user);
            var pos = user.zone.location.position.split(',');
            var nearby_user_loc = {lat: parseFloat(pos[0]), lng: parseFloat(pos[1])};
            var contentUser = $('<content>').addClass('user_info');
            var userImage = $('<img>').attr('src', user.member.image);
            var userName = $('<p>').text(user.member.username);
            var userEmail = $('<p>').text(user.member.email);
            contentUser.append(userImage, userName, userEmail);
            var infowindow = new google.maps.InfoWindow({
                content: contentUser.html(),
                position: nearby_user_loc

            });
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(nearby_user_loc.lat, nearby_user_loc.lng),
                animation: google.maps.Animation.DROP,
                title: (user.member.username) + '  is  ' + 'Checked-in',
                map: map
            });
            marker.addListener('click', function () {
                infowindow.open(map, marker);
            });
            markers.push(marker);
        })
    }

    function postCheckin(user_loc, meters) {
        if (typeof $meters === "undefined") {
            var $meters = 500;
        }
        $.ajax({

            url: '/members/check_ins/',   // Target Server
            method: 'POST',                                            // Request Verb
            data: {
                'lat': user_loc.lat,
                'lng': user_loc.lng,
                'radius': meters
            },                                                       // Request Params
            success: function (rsp) {                                // Success Handler
                swal({
                    imageUrl: 'https://premium.wpmudev.org/blog/wp-content/uploads/2015/09/nasa-scroll2.gif',
                    type: "success",
                    title: "You are Checked-In!"
                })
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
                swal("Error!", "You are not Checked-In!", "error");
            }
        });
    }


    function get_loc(meters) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var user_loc = {lat: position.coords.latitude, lng: position.coords.longitude};
            postCheckin(user_loc, meters);
            getCheckin(user_loc, meters);
        });
    }


    $('#check_in').on('click', function (event) {
        event.preventDefault();
        // marker.setMap(null);
        get_loc(meters);
    });


    function getCheckin(user_loc, meters) {
        if (typeof $meters === "undefined") {
            var $meters = 500;
        }
        $.ajax({
            url: '/members/check_ins/',   // Target Server
            method: 'GET',                                            // Request Verb
            data: {
                'lat': user_loc.lat,
                'lng': user_loc.lng,
                'radius': meters
            },                                                      // Request Params
            success: function (rsp) {                                // Success Handler
                var nearby_users = rsp;
                add_users(nearby_users);
                console.log(nearby_users)
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
            }
        });
    }

})();