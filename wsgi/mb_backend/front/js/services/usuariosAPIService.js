angular.module("receitasFamilia").service("usuarioAPI",function($http, config){   

    this.postCadastrarUsuario = function(usuario){
        return $http.post(config.baseUrl +"/users/?format=json",usuario);
    };         
    this.postLogin = function(username,password){       
        return $http.post(config.baseUrl +"/api-auth/login/?next=/app/users/",{username: username, password:password});
    };   
});