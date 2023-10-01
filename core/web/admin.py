from django.contrib import admin
from .models import Post, Course, Mentor, Url, FooterLinkPage, FooterLinkContact, FooterLinkBlog

admin.site.register(Post)
admin.site.register(Course)
admin.site.register(Mentor)
admin.site.register(Url)
admin.site.register(FooterLinkPage)
admin.site.register(FooterLinkContact)
admin.site.register(FooterLinkBlog)
