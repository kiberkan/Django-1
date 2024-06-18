from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    """Главная страница"""
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы найдете информацию о проекте и обо мне.</p>
    <a href="/about">О себе</a>
    """
    logger.info('Посещение главной страницы')
    return HttpResponse(html)

def about(request):
    """Страница "О себе" """
    html = """
    <h1>О себе</h1>
    <p>Меня зовут Антон, и я пытаюсь разобраться в Django.</p>
    <p>Я учусь создавать веб-приложения, и этот сайт - мой первый шаг хD.</p>
    <a href="/">На главную</a>
    """
    logger.info('Посещение страницы "О себе"')
    return HttpResponse(html)