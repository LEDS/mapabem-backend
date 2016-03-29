angular.module("receitasFamilia").controller("detalhesCategoriaCtrl", function($scope,$routeParams,receitas,categoria){
    $scope.categoria = categoria.data;
    $scope.receitas= receitas.data;            
});