from django.db import models as m
from tinymce.models import HTMLField
from uuid import uuid4

class Subject(m.Model):

    id = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")
    
    title = m.CharField(max_length = 200, verbose_name = "Title")
    slug = m.SlugField(unique = True, verbose_name = "Slug")
    
    image = m.ImageField(upload_to = 'subjects/', blank = True, null = True, verbose_name = "Image")

    created_at = m.DateTimeField(auto_now_add = True, verbose_name = "Created At")

    def __str__(self):

        return self.title

    class Meta:

        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Field(m.Model):

    id = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")
    
    subject = m.ForeignKey(Subject, on_delete = m.DO_NOTHING, blank = True, null = True, verbose_name = "Subject")

    def __str__(self):
        
        return self.title

    class Meta:

        verbose_name = "Field"
        verbose_name_plural = "Fields"


class Topic(m.Model):

    id = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")
    
    subject = m.ForeignKey(Subject, on_delete = m.CASCADE, related_name = 'topics', verbose_name = "Subject")
    field = m.ForeignKey(Field, on_delete = m.CASCADE, related_name = 'topics', verbose_name = "Subject")
    
    title = m.CharField(max_length = 200, verbose_name = "Title")
    slug = m.SlugField(unique = True, verbose_name = "Slug")
    
    created_at = m.DateTimeField(auto_now_add = True, verbose_name = "Created At")

    def __str__(self):

        return f"{self.subject.title} - {self.title}"

    class Meta:

        verbose_name = "Topic"
        verbose_name_plural = "Topics"


class Lesson(m.Model):

    id = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")
    topic = m.ForeignKey(Topic, on_delete = m.CASCADE, related_name = 'lessons', verbose_name = "Topic")
    
    title = m.CharField(max_length = 200, verbose_name = "Title")
    slug = m.SlugField(unique = True, verbose_name = "Slug")
    
    content = HTMLField(verbose_name = "Content")  # TinyMCE for rich-text lesson content
    
    created_at = m.DateTimeField(auto_now_add = True, verbose_name = "Created At")
    updated_at = m.DateTimeField(auto_now = True, verbose_name = "Updated At")

    def __str__(self):

        return f"{self.topic.subject.title} - {self.topic.title} - {self.title}"

    class Meta:

        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Task(m.Model):

    id = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")
    
    lesson = m.ForeignKey(Lesson, on_delete = m.CASCADE, related_name = 'tasks', verbose_name = "Lesson")
    
    question = HTMLField(verbose_name = "Question")  # TinyMCE for task question
    explanation = HTMLField(verbose_name = "Explanation")  # TinyMCE for task explanation
    
    correct_answer = m.CharField(max_length = 255, verbose_name = "Correct Answer")
    answer2 = m.CharField(max_length = 255, verbose_name = "Answer 2")
    answer3 = m.CharField(max_length = 255, verbose_name = "Answer 3")
    answer4 = m.CharField(max_length = 255, verbose_name = "Answer 4")
    
    created_at = m.DateTimeField(auto_now_add = True, verbose_name = "Created At")
    updated_at = m.DateTimeField(auto_now = True, verbose_name = "Updated At")

    def __str__(self):

        return f"Task for {self.lesson.title}"

    class Meta:

        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class AnswerOption(m.Model):

    id = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")
    
    task = m.ForeignKey(Task, on_delete = m.CASCADE, related_name = 'options', verbose_name = "Task")
    
    text = m.CharField(max_length = 255, verbose_name = "Text")

    def __str__(self):

        return self.text

    class Meta:

        verbose_name = "Answer Option"
        verbose_name_plural = "Answer Options"
