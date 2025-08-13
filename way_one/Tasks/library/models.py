from django.db import models

class Author(models.Model):
    name = models.CharField(
        max_length=120
    )
    birth_year = models.IntegerField()



    def __str__(self):
        return f'{self.name}'
    




class Book(models.Model):
    title = models.CharField(max_length=120)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author , on_delete=models.CASCADE # TODO bussuness logic may be change 
    )

    def __str__(self):
        return f'{self.title}--{self.author}'