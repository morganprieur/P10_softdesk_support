
from django.db import models 
from django.contrib.auth.models import User 


PROJECT_TYPE = ( 
    ("ALL", "ALL"), 
    ("BACK", "BACK-END"), 
    ("FRONT", "FRONT-END"), 
    ("IOS", "IOS"), 
    ("AND", "ANDROID"), 
) 


class Project(models.Model): 
    author = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE, 
        related_name='project_author', 
        # blank=True, 
        # null=True 
    ) 
    name = models.CharField(max_length=100)  # , blank=True, null=True 
    description = models.TextField(blank=True, null=True) 
    type = models.CharField( 
        max_length=9, 
        choices=PROJECT_TYPE, 
        default=PROJECT_TYPE[1][0] 
    ) 
    created_time = models.DateTimeField( 
        auto_now_add=True 
    ) 

""" 
    Seuls les contributeurs d’un projet peuvent accéder à ce dernier. 
        Seuls les contributeurs peuvent accéder aux ressources qui référencent un projet 
            issue 
            comment
    Le contributor est une ressource spécifique, qui lie un utilisateur à un projet.
""" 

