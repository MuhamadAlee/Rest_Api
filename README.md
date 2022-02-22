# Rest_Api in Django

Here are some steps to follow

1) create and activate virtual envirnment.
      
        virtualenv -p python3 env
        source env/bin/activate
        
2) Install dependenceies

        pip install django
        pip install djangorestframework
        
3) Create new project in django

        django-admin startproject my_project

4) Move to my_project directory
        
        cd my_project
               
5) Create new app in django

        django-admin startapp my_app
         
6) Now you will have following directory structure

         my_project
            |
            |
            |--- my_project.
            |
            |
            |--- my_app.
            |
            |
            |--- manage.py.
            
7) Register app in "my_project/my_project/settings.py"
        
        INSTALLED_APPS = [
            ......
            ......
            ......
            
            'my_app',
            'rest_framework',

        ]
8) Make urls.py inside my_app
            
            touch urls.py
            
9) Make functionality in my_app/views.py

            from rest_framework.decorators import api_view
            from rest_framework.response import Response

            @api_view(['GET', 'POST'])
            def Helloworld(request):
                if request.method == 'POST':
                    return Response({"message": "Got some data!", "data": request.data.get("text")})
                return Response({"message": "Hello, world!"})
               

10) Add urls for "my_project/my_app/urls.py"

            from .views import HelloWorld
            
            urlpatterns = [
                  ....
            path("",HelloWorld),
            
            ]
            
11) Now, make urls of my_project refers to the urls of my_app inside "myproject/my_project/urls.py"
            
            urlpatterns = [
                  ....
            path("",include("my_app.urls")),
            
            ]
      
 
        
12) Now run server

            ./manage.py runserver
            

13) You can access it by request
            
            import requests
            resp=requests.post("http://127.0.0.1:8000/",data={"text":"ALI"})
            res.json()

            
