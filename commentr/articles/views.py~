from django.http import HttpResponse
#from django.shortcuts import render, redirect
#from django.contrib import auth
from django import forms

from articles.models import *

def index(request):
    return HttpResponse("<h1>Project Home</h1>  <a href='{% url articles %}'>Articles</a>")

def article_view(request):
    articles = Article.objects.all()

    #build string for list of articles
    response = "<h1>Articles List</h1>"
    for article in articles:
        response += "<p><a href='{" + article.title + "}'>"
        response += str(article) + "</a></p>"
    return HttpResponse(response)

def display_comment(comment):
    built_string = ""
    if(comment.parent != None):
        built_string += "<ul>"
    built_string += "<li>"
    built_string += str(comment)
    children = Comment.objects.filter(parent=comment)
    for child in children:
        built_string += display_comment(child)
    built_string += "</li>"
    if(comment.parent != None):
        built_string += "</ul>"
    return built_string

def comments(request, article_name):
    article_name = article_name[1:len(article_name)-1]
    comments = Comment.objects.filter(article__title=article_name)
    response = "<h2> Comments for " + article_name + "</h2>"
    if comments.count() == 0:
        response += "<p> No comments available </p>"
    else:
        response += "<ul>"
        for comment in comments:
            if(comment.parent == None):
                response += display_comment(comment)
        response += "</ul>"
    return HttpResponse(response)

