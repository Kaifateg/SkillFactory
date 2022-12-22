from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    rating_author = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating_news'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.user.comment_set.aggregate(commentRating=Sum('rating_comment'))
        comRat = 0
        comRat += commentRat.get('commentRating')

        self.rating_author = pRat * 3 + comRat
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=128, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    CHOICE = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    type_category = models.CharField(max_length=2, choices=CHOICE, default=NEWS)
    name_news = models.CharField(max_length=255)
    text_news = models.TextField()
    rating_news = models.IntegerField(default=0)
    time_create_post = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_news += 1
        self.save()

    def dislike(self):
        self.rating_news -= 1
        self.save()

    def preview(self):
        return '{}...'.format(self.name_news[0:123])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.TextField()
    time_create_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -=1
        self.save()
