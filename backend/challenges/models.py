from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    goodreads_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
class Book(models.Model):
    goodreads_id = models.CharField(max_length=50, unique=True)  
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)  
    isbn = models.CharField(max_length=20, null=True, blank=True)  
    isbn13 = models.CharField(max_length=20, null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)  # Can be populated using an API
    goodreads_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="user_books")
    status = models.CharField(
        max_length=20, 
        choices=[
            ("read", "Read"),
            ("currently-reading", "Currently Reading"),
            ("to-read", "To Read"),
        ]
    )
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    private_notes = models.TextField(null=True, blank=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    date_read = models.DateField(null=True, blank=True)
    read_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    query = models.TextField(help_text="Query defining the challenge criteria")  # e.g., 'read a book for every year from 2000 to 2001'
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)  # Optional: Set start date for challenge
    end_date = models.DateField(null=True, blank=True)  # Optional: Set deadline for challenge
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="challenges")  # Assigns the challenge to a user
    is_public = models.BooleanField(default=True)  # Whether the challenge is visible to others
    max_books = models.PositiveIntegerField(null=True, blank=True, help_text="Max number of books for this challenge")

    def __str__(self):
        return self.title