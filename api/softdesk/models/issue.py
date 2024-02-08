
from django.db import models 
from django.contrib.auth.models import User 
from softdesk.models import Project 


ISSUE_STATUS = ( 
    ("TODO", "TO DO"), 
    ("IP", "IN PROGRESS"), 
    ("FINISHED", "FINISHED"), 
) 
ISSUE_PRIORITY = ( 
    ("LOW", "LOW"), 
    ("MEDIUM", "MEDIUM"), 
    ("HIGH", "HIGH"), 
) 
ISSUE_TAG = ( 
    ("BUG", "BUG"), 
    ("FEATURE", "FEATURE"), 
    ("TASK", "TASK"), 
) 


class Issue(models.Model): 

    author = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE, 
        related_name='project_author' 
    ) 
    project = models.ForeignKey( 
        Project, 
        on_delete=models.CASCADE, 
        related_name='issue_project' 
    ) 
    status = models.CharField( 
        max_length=6, 
        choices=ISSUE_PRIORITY, 
        default=ISSUE_PRIORITY.TODO 
    ) 
    priority = models.CharField( 
        max_length=8, 
        choices=ISSUE_STATUS, 
        default=ISSUE_STATUS.LOW 
    ) 
    tag = models.CharField( 
        max_length=7, 
        choices=ISSUE_TAG, 
    ) 
    created_time = models.DateTimeField( 
        auto_now_add=True 
    ) 

""" 
    author
        PK user
    project
    statut de progression
        To Do - défaut
        In Progress
        Finished
    priorité
        défaut ? non 
        LOW
        MEDIUM
        HIGH
    balise 
        défaut ? non 
        bug
        feature
        task 
""" 
