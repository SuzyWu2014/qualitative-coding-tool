from django.db import models


class Goal(models.Model):
    """Goal of an expalnation unit"""
    goal_id = models.AutoField(primary_key=True)
    goal = models.CharField(max_length=16)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.goal


class Role(models.Model):
    """Role for an expalnation unit"""
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=16)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.role


class Notation(models.Model):
    """Notation used for an expalnation unit"""
    notation_id = models.AutoField(primary_key=True)
    notation = models.CharField(max_length=16)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.notation


class Explanation(models.Model):
    """Explanation unit"""
    explanation_id = models.AutoField(primary_key=True)
    explanation = models.CharField(max_length=16)
    source_link = models.URLField(max_length=256)
    evernote_link = models.URLField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.explanation


class Code(models.Model):
    """Code object for each explanation unit"""
    code_id = models.AutoField(primary_key=True)
    explanation = models.ForeignKey(Explanation)
    position = models.IntegerField()
    goal = models.ForeignKey(Goal)
    role = models.ForeignKey(Role)
    notations = models.ManyToManyField(Notation)
    is_partial = models.BooleanField(default=False)
    is_emphasized = models.BooleanField(default=False)
    has_many = models.BooleanField(default=False)
    description = models.CharField(max_length=256, blank=True)

    def notationlist(self):
        return list(self.notations.all())
