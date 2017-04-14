# Django no OpenShift

##Introdução
> Neste respositório é apresentado um exemplo de como um projeto Django deve ser estruturado para funcionar na infraestrutura do OpenShift. A documentação foi retirada da git do OpenShift que pode ser acessada no [link](http://github.com/openshift/django-example).
Além disso, esse repositório está configurado para trabalhar com [Travi-CI](http://travis-ci.org/) e [Sonarqube](http://www.sonarqube.org/)




##Sincronizando com tudo!

Admin user name and password
----------------------------
Use `rhc ssh` to log into python gear and run this command:

	python $OPENSHIFT_REPO_DIR/wsgi/myproject/manage.py createsuperuser

You should be now able to login at:

	http://django-$yournamespace.rhcloud.com/admin/
	
