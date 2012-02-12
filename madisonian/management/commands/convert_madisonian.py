import re

from django.core.management.base import BaseCommand, CommandError

from armstrong.core.arm_sections import models as section_models

from madisonian import models as mad_models

# Need to convert:
#
# 1. Sections
# 2. News
# 3. Users

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clear_tables()
        self.convert_sections()


    def convert_sections(self):
        for section in mad_models.Sections.objects.all().order_by('priority'):
            slug = re.sub(r"\W", "", section.section.lower())
            section_models.Section.objects.create(title=section.section, slug=slug)


    def clear_tables(self):
        self.clear_sections()

    def clear_sections(self):
        section_models.Section.objects.all().delete()