(function loadPages() {
    "use strict";
    var $profilePage = $('#profile');
    var $mapPage = $('#map');
    var $settingsPage = $('#settings');

    $profilePage.on('click', function (event) {
        $mapPage.hide();
        $settingsPage.hide();
        $profilePage.show(event).addClass('ui-btn-active')

    });

    $mapPage.on('click', function (event) {
        $profilePage.hide();
        $settingsPage.hide();
        $mapPage.show(event).addClass('ui-btn-active')

    });

    $settingsPage.on('click', function (event) {
        $profilePage.hide();
        $mapPage.hide();
        $settingsPage.show(event).addClass('ui-btn-active')

    })
})();