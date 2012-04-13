import datetime
import re

from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites import models as sites_models

from armstrong.apps.articles import models as article_models
from armstrong.core.arm_sections import models as section_models
from armstrong.core.arm_wells import models as well_models

from madisonian import models as mad_models

# Need to convert:
#
# 1. Sections
# 2. News
# 3. Users

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.slug_ctr = 0
        self.clear_tables()
        self.convert_sections()
        self.convert_articles()
        self.add_well()

    def convert_sections(self):
        for section in mad_models.Sections.objects.all().order_by('priority'):
            slug = self.slugify(section.section)
            section_models.Section.objects.create(title=section.section, slug=slug)

    def convert_articles(self):
        pass
        for news in mad_models.News.objects.filter(issue_date__gt=datetime.date(2011,12,31)):
            slug = re.sub(r"\W", "", news.caption.lower())
            if not slug:
                slug = self.junk_slug()
            try:
                article_models.Article.objects.get(slug=slug)
                slug = self.junk_slug()
            except article_models.Article.DoesNotExist:
                pass
            pub_date = datetime.datetime.strptime("%s 00:00:00" % news.issue_date, "%Y-%m-%d %H:%M:%S")
            article = article_models.Article(title=news.caption,
                                             slug=slug[:50],
                                             summary=news.preview,
                                             body=news.full_story,
                                             pub_date=pub_date,
                                             pub_status='P',)
            article.save()
            article.sites.add(sites_models.Site.objects.all()[0])
            article.sections.add(section_models.Section.objects.get(full_slug=self.slugify(news.section)))
            article.save()


    def clear_tables(self):
        self.clear_sites()
        self.clear_sections()
        self.clear_articles()

    def clear_sites(self):
        site = sites_models.Site.objects.all()[0]
        site.domain='wintersetmadisonian.com'
        site.name='wintersetmadisonian.com'
        site.save()

    def clear_sections(self):
        section_models.Section.objects.all().delete()

    def clear_articles(self):
        article_models.Article.objects.all().delete()

    def slugify(self, words):
        return re.sub(r"\W", "", words.lower())

    def junk_slug(self):
        self.slug_ctr += 1
        return str(self.slug_ctr)

    def add_well(self):
        type = well_models.WellType.objects.create(title='front_page', slug='front_page')
        well_models.Well.objects.create(pub_date=datetime.datetime.now(), type=type)