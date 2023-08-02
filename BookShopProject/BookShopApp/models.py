from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    slug = models.SlugField(unique=True)
    img = models.URLField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.slug

class Review(models.Model):
    from_name = models.CharField(max_length=100)
    from_surname = models.CharField(max_length=100)
    tags = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.from_name} {self.from_surname}"   

# from django import forms

# class ReviewForm(forms.ModelForm):
#     is_member = forms.BooleanField(required=False)

#     class Meta:
#         model = Review
#         fields = ['from_name', 'from_surname', 'tags', 'rating', 'is_member']     
