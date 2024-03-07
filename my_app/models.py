from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=255)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class QuizResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()

# Добавим поля для создания тестовых данных
def create_test_data():
    # Создаем викторину
    quiz = Quiz.objects.create(title="Простая викторина")

    # Создаем вопросы для викторины
    question1 = Question.objects.create(quiz=quiz, text="Сколько будет 2 + 2?")
    question2 = Question.objects.create(quiz=quiz, text="Какое столицей является Париж?")

    # Создаем варианты ответов для каждого вопроса
    Answer.objects.create(question=question1, text="3", is_correct=False)
    Answer.objects.create(question=question1, text="4", is_correct=True)
    Answer.objects.create(question=question1, text="5", is_correct=False)

    Answer.objects.create(question=question2, text="Лондон", is_correct=False)
    Answer.objects.create(question=question2, text="Берлин", is_correct=False)
    Answer.objects.create(question=question2, text="Париж", is_correct=True)

    # Создаем пользователя и результат викторины
    user = User.objects.create(username="test_user", password="test_password")
    quiz_result = QuizResult.objects.create(user=user, quiz=quiz, score=0)

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title