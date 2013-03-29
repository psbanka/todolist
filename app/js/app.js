angular.module('phonecat', []).
    config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/index.html', {templateUrl: 'partials/welcome.html', controller: PhoneListCtrl}).
        when('/phones', {templateUrl: 'partials/phone-list.html', controller: PhoneListCtrl}).
        otherwise({redirectTo: '/index.html'});
    }]);