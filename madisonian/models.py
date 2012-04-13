import datetime

from django.db import models

from armstrong.core.arm_sections import models as arm_sections_models

class MadSectionManager(models.Manager):
    def get_active_sections(self):
        sections = []
        for section in self.all():
            if section.content_content_alternates.filter(pub_date__gte=datetime.date.today() - datetime.timedelta(6*365/12)):
                sections.append(section)
        return sections

class MadSection(arm_sections_models.Section):
    objects = MadSectionManager()

    class Meta:
        proxy = True

# BELOW:
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

class Ads(models.Model):
    ad_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=3, blank=True)
    status = models.CharField(max_length=3, blank=True)
    pic_file = models.CharField(max_length=600, blank=True)
    link_to = models.CharField(max_length=300)
    class Meta:
        db_table = u'ads'

class Email(models.Model):
    email = models.CharField(max_length=150, primary_key=True)
    class Meta:
        db_table = u'email'

class Issues(models.Model):
    issue_date = models.DateField(primary_key=True)
    issue_num = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issues'

class News(models.Model):
    issue_date = models.DateField(primary_key=True)
    news_num = models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=600, blank=True)
    sub_caption = models.CharField(max_length=600, blank=True)
    preview = models.TextField(blank=True)
    full_story = models.TextField(blank=True)
    free = models.CharField(max_length=3, blank=True)
    preview_pic = models.CharField(max_length=150, blank=True)
    pic_1 = models.CharField(max_length=150, blank=True)
    pic_2 = models.CharField(max_length=150, blank=True)
    pic_3 = models.CharField(max_length=150, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=90, blank=True)
    caption_1 = models.TextField(blank=True)
    caption_2 = models.TextField(blank=True)
    caption_3 = models.TextField(blank=True)
    author = models.CharField(max_length=90, blank=True)
    viewed = models.IntegerField(null=True, blank=True)
    third_headline = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'news'

class Sections(models.Model):
    section = models.CharField(max_length=60, primary_key=True)
    parent_child = models.CharField(max_length=3, blank=True)
    free = models.CharField(max_length=3, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sections'

class Session(models.Model):
    session_id = models.CharField(max_length=90, primary_key=True)
    session_var = models.CharField(max_length=60, primary_key=True)
    session_val = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'session'

class Users(models.Model):
    user_id = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)
    user_name = models.CharField(max_length=90, blank=True)
    user_auth = models.IntegerField(null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    card_holder_name = models.CharField(max_length=90, blank=True)
    street_address = models.CharField(max_length=90, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=6, blank=True)
    zip = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=90, blank=True)
    phone = models.CharField(max_length=60, blank=True)
    credit_card_processed = models.CharField(max_length=3, blank=True)
    total = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    product_id = models.CharField(max_length=30, blank=True)
    quantity = models.CharField(max_length=30, blank=True)
    expiration = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'users'