angular.module("receitasFamilia").service("receitasAPI",function($http, config){
   this.getReceitas = function(){
        return $http.get(config.baseUrl +"/receita/?format=json");
    };

    this.getReceita = function(id){
        return $http.get(config.baseUrl +"/receita/"+id+"/?format=json");
    };

    this.getReceitasInCategoria = function(id){
      return $http.get(config.baseUrl + "/receita/categoria/"+id+"/?format=json");
    };
});
