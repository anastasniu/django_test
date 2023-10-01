from django.db import models


class Post(models.Model):
    # Карточки информации
    title = models.CharField(max_length=200)
    content = models.TextField()
    icon = models.ImageField(upload_to='image/', null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    # Опции курсов
    option = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    more_information = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Mentor(models.Model):
    # Карточки менторов
    name = models.CharField(max_length=100)
    description = models.TextField()
    education = models.TextField()
    image = models.ImageField(upload_to='image/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Url(models.Model):
    # Ссылки для кнопок на галвной страницы
    title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class FooterLinkPage(models.Model):
    # Ссылки для футера стобец Page
    page_title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.page_title
    pass


class FooterLinkBlog(models.Model):
    # Ссылки для футера столбец Blog
    blog_title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.blog_title
    pass


class FooterLinkContact(models.Model):
    # Ссылки для футера столбец Contact
    contact_title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.contact_title
    pass
