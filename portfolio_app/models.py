from django.db import models
#project model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='projects/')
    Source_link = models.URLField(max_length=200, blank=True)
    Live_Link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
#service models
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='services/')  

    def __str__(self):
        return self.name


#edu modls


class Education(models.Model):
    Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='education/')
    Starting_Date = models.CharField(max_length=20)
    Ending_Date = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


#experience model
class Experience(models.Model):
    post = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    from_date = models.CharField(max_length=50)
    to_date = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.post} at {self.company_name}"


#about me footer model
class AboutMe(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Me"



#mini project footer model (comming soon : ))
class MiniProjects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    live_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


