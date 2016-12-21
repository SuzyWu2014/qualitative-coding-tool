from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):
    """Tag object"""
    GOAL_CHOICE = (
        ('Problem', 'Problem'),
        ('Algorithm', 'Algorithm'),
        ('Implementation', 'Implementation'),
        )
    ROLE_CHOICE = (
        ('Definition', 'Definition'),
        ('Example', 'Example'),
        ('Application', 'Application'),
        ('Variant', 'Variant'),
        ('Analogy', 'Analogy'),
        ('Background', 'Background'),
        ('Performance', 'Performance'),
        ('Ideas', 'Ideas'),
        ('Proof', 'Proof'),
        ('Constraint', 'Constraint'),
        )
    TRAIT_CHOICE = (
        ('Partial', 'Partial'),
        ('Emphasised', 'Emphasised'),
        ('None', 'None'),
        )
    NOTATION_CHOICE = (
        ('English', 'English'),
        ('Math', 'Math'),
        ('Pseudocode', 'Pseudocode'),
        ('Code', 'Code'),
        ('Table', 'Table'),
        ('List', 'List'),
        ('Diagram', 'Diagram'),
        ('Plot', 'Plot'),
        ('Picture', 'Picture'),
        ('Sequence', 'Sequence'),
        ('DS-diagram', 'DS-diagram'),
        ('Animation', 'Animation'),
        )

    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goal = models.CharField(max_length=200, choices=GOAL_CHOICE, default='Problem')
    role = models.CharField(max_length=200, choices=ROLE_CHOICE, default='definition')
    notation = models.CharField(max_length=200, choices=NOTATION_CHOICE, default='English')
    trait = models.CharField(max_length=200, choices=TRAIT_CHOICE, default='None')
    order = models.PositiveIntegerField()


class Explanation(models.Model):
    """Explanation object"""
    def __init__(self, arg):
        super(Explanation, self).__init__()
        self.arg = arg

    exp_id = models.CharField(max_length=5, primary_key=True)
    source_link = models.URLField()
    evernote_link = models.URLField()
    Tags = models.ManyToManyField(Tag, through='Membership', through_fields=('tag', 'explanation'))


class Membership(models.Model):
    tag = models.ForeignKey(Tag)
    explanation = models.ForeignKey(Explanation)
