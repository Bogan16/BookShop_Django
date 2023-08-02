from django.shortcuts import render
from .models import Book, Review

def homepage(request):
    books = Book.objects.all()
    reviews = Review.objects.all()
    if request.method == 'POST':
        from_name = request.POST.get('from_name')
        from_surname = request.POST.get('from_surname')
        tags = request.POST.get('tags')
        rating = request.POST.get('rating')
        is_member = request.POST.get('is_member', False) == 'on'

        review = Review.objects.create(
            from_name=from_name,
            from_surname=from_surname,
            tags=tags,
            rating=rating,
            is_member=is_member,
        )
        review.save()
    return render(request, 'BookShopApp/homepage.html', {'books': books, 'reviews': reviews})