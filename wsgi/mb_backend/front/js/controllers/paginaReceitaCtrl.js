angular.module("receitasFamilia").controller("paginaReceitaCtrl", function($scope, $routeParams, receita){

    $scope.receita = receita.data;
});
