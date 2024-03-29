from users.models import (Contributor, UserProfile) 
from softdesk.models import (Comment, Issue, Project) 
# from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User, Group 
from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver 
from datetime import datetime 


@receiver(post_save, sender=Project) 
def create_contributor(sender, instance, created, **kwargs): 
    """ When a Project instance is created: 
            creates a Contributor.  
        Args:
            sender (Project): the model sends a signal when an instance is created 
            instance (Project): the just created Project 
            created (bool): the Project instance is created True/False : trigger. 
                If False, the program exits the method.  
    """ 
    # Création d'un Contributor. 
    if created: 
        print(instance) 
        new_contrib = Contributor.objects.create( 
            user=instance.author, 
            project=instance 
        )  
        new_contrib.save() 


@receiver(post_save, sender=Issue) 
def Change_comment_author(sender, instance, **kwargs): 
    """ When an Issue instance is updated: 
            Check if the author has been changed. 
            If yes : update the comment in the same way.  
        Args:
            sender (Issue): the model sends a signal when an instance is created 
            instance (issue): the just created issue 
            created (bool): the issue is created True/False : trigger. 
                If False, the program exits the method.  
    """ 
    # Modification de l'auteur d'un comment. 
    issue = instance 
    comments = Comment.objects.filter(issue=issue.id) 
    for comment in comments: 
        if comment.author != issue.author: 
            comment.author = issue.author 
            comment.save() 
            # print('comment : ', comment.author, ' issue : ', issue.author) 


@receiver(post_delete, sender=UserProfile) 
def delete_profile(sender, instance, **kwargs): 
    """ When a UserProfile instance is deleted: 
            deletes the linked user.  
        Args:
            sender (UserProfile): the model sends a signal when an instance is deleted. 
            instance (UserProfile): the just deleted UserProfile. 
    """ 
    User.objects.get(id=instance.user.id).delete() 

