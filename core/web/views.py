from django.shortcuts import render
from .models import Post, Course, Mentor, Url, FooterLinkPage, FooterLinkContact, FooterLinkBlog


def content_view(request):
    posts = Post.objects.all()
    course = Course.objects.all()
    mentor = Mentor.objects.all()
    url = Url.objects.all()
    footer_links_page = FooterLinkPage.objects.all()
    footer_links_contact = FooterLinkContact.objects.all()
    footer_links_blog = FooterLinkBlog.objects.all()
    context = {
        'course': course,
        'post': posts,
        'mentor': mentor,
        'url': url,
        'footer_links_page': footer_links_page,
        'footer_links_contact': footer_links_contact,
        'footer_links_blog': footer_links_blog,
    }
    return render(request, 'index.html', context)
