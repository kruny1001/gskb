# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Genesets2(models.Model):
    label = models.CharField("Label",max_length=585, blank=True, primary_key=True)
    species = models.CharField("Species Type",max_length=765)
    source = models.CharField("Source",max_length=39, blank=True)
    regtype = models.CharField("Regulation Type",max_length=33, db_column='regType', blank=True) # Field name made lowercase.
    chip = models.CharField("Chip Type", max_length=81, blank=True)
    detailsurl = models.CharField("Details URL", max_length=1206, db_column='detailsUrl', blank=True) # Field name made lowercase.
    descriptionbrief = models.CharField("Brief Description", max_length=1920, db_column='descriptionBrief', blank=True) # Field name made lowercase.
    descriptionfull = models.TextField("Full Description", db_column='descriptionFull', blank=True) # Field name made lowercase.
    pubmed = models.CharField("PubMed ID", max_length=765, blank=True)
    firstauthor = models.CharField("Publication's first author", max_length=483, db_column='firstAuthor', blank=True) # Field name made lowercase.
    papertitle = models.CharField("Publication's title", max_length=684, db_column='paperTitle', blank=True) # Field name made lowercase.
    year = models.DecimalField("Publication Year", null=True, max_digits=5, decimal_places=0, blank=True)
    citation = models.CharField("Publication Citation", max_length=309, blank=True)
    comment = models.CharField("Comment", max_length=144, blank=True)
    ngenes = models.IntegerField("Number Of Genes", null=True, db_column='nGenes', blank=True) # Field name made lowercase.
    genes = models.TextField("Original Gene IDs", blank=True)
    genessym = models.TextField("Gene Symbols", db_column='genesSym', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'genesets2'
        #ordering = ['source','year','label']

    def __unicode__(self):
        return self.label
