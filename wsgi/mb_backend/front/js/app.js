angular.module("receitasFamilia",["ngMessages","ngRoute"]);
angular.module("receitasFamilia").config(function($httpProvider){      
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';         
});