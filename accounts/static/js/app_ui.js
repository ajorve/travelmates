(function loadPages() {
    "use strict";
    var $profilePage = $('#profile');
    var $mapPage = $('#map-canvas');
    var $settingsPage = $('#settings');

    $profilePage.on('click', function (event) {
        // $mapPage.hide();
        // $settingsPage.hide();
        this.addClass('ui-btn-active')

    });

    $mapPage.on('click', function (event) {
        // $profilePage.hide();
        // $settingsPage.hide();
        this.addClass('ui-btn-active')

    });

    $settingsPage.on('click', function (event) {
        // $profilePage.hide();
        // $mapPage.hide();
        this.addClass('ui-btn-active')

    })
})();