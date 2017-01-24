from django.contrib import admin
from .models import Goal, Role, Explanation, Notation, Code


class CodeInline(admin.TabularInline):
    model = Code


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('goal', 'description')
    inlines = [CodeInline, ]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('role', 'description')
    inlines = [CodeInline, ]


@admin.register(Notation)
class NotationAdmin(admin.ModelAdmin):
    empty_value_display = '-- empty --'
    list_display = ('notation', 'description')


@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
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
    list_filter = ['notations', 'explanation', 'role', 'goal']
    filter_horizontal = ['notations']
    show_full_result_count = True
    ordering = ['explanation', 'position']
    list_per_page = 50
    radio_fields = {"goal": admin.HORIZONTAL}
    save_on_top = True
