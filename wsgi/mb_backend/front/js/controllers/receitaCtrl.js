angular.module("receitasFamilia").controller("receitaCtrl", function($scope,receitasAPI,receitas){
    $scope.receitas= receitas.data;      
});