from django.contrib import admin
from .models import Subject, Topic, Lesson, Task, Field, AnswerOption

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "image", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]
    list_filter = ["created_at"]

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ["id", "subject"]
    search_fields = ["subject__title"]
    list_filter = ["subject"]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "subject", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "subject__title"]
    list_filter = ["subject", "created_at"]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "topic", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content", "topic__title"]
    list_filter = ["topic", "created_at", "updated_at"]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "lesson", "question", "correct_answer", "created_at", "updated_at"]
    search_fields = ["question", "lesson__title"]
    list_filter = ["lesson", "created_at", "updated_at"]

@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ["id", "task", "text"]
    search_fields = ["text", "task__question"]
    list_filter = ["task"]
