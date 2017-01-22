from django.contrib import admin
from .models import Goal, Role, Explanation, Notation, Code


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('goal', 'description')


@admin.register(Role)
class GoalAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('role', 'description')


@admin.register(Notation)
class GoalAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('notation', 'description')


@admin.register(Explanation)
class GoalAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('explanation',
                    'source_link',
                    'evernote_link',
                    'description')


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('explanation',
                    'position',
                    'goal',
                    'role',
                    'is_partial',
                    'is_emphasized',
                    'has_many'
                    )
    list_filter = ['notations']
    filter_horizontal = ['notations']
    show_full_result_count = ['explanation']
