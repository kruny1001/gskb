from django import forms
from django.utils.safestring import mark_safe

from models import Genesets2

# Options for sources from which to load.
# Note: empty source choices will allow for the downloading of empty
#       alternatively-formatted output (like CSV and xml). gssearch()
#       has logic to prevent this

from django.db.models import Count

def genSortedList(obj, col, includeAll = True):
    '''Generate a list of options, sorted by their occurence, suitable for
    inclusion as a 'choices' entry.
    "obj" refers to which Model subset to select from
    "col" is the column to use'''

    ret = []

    # Include all
    if includeAll:
        ret.append(('all', 'All'))

    raw = obj.values(col).annotate(Count(col))
    counts =  [(x[col],x[col+'__count']) for x in raw]
    counts = sorted(counts, reverse=True, key=lambda x: x[1])
    ret.extend([(x[0],x[0]) for x in counts])
    return ret

source_choices   = genSortedList(Genesets2.objects,"source")
species_choices  = genSortedList(Genesets2.objects,"species")

encoding_choices = (('html','Web Page'),
                  ('csv','CSV (includes additional fields)'),
                  ('xml', 'XML (includes additional fields)'),
                  ('json', 'JSON (includes additional fields)'),)

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
      def render(self):
              return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class SearchForm(forms.Form):
    search = forms.CharField(required=False,max_length=100, min_length=0,
                             help_text='''
                             <br>Fields searched: Geneset label, First Author,
                             Brief Description, Genes, Gene Symbols and
                             Citation.<br>
                             Examples (remove quotes when using): Gene names
                             (like "WRKY" or "GAPDH"),
                             keywords (like "cold"), or first authors (like
                             "Mueller")''')
    sources = forms.ChoiceField(required=True,
                choices=source_choices, initial="all")

    species = forms.ChoiceField(required=True, label="Species",
                                choices = species_choices, initial="all")

    encoding = forms.ChoiceField(label='Format', choices=encoding_choices,
                                 initial='html')

   # sources = forms.ChoiceField(required=True,
   #             widget = forms.RadioSelect(renderer=HorizontalRadioRenderer,
   #             attrs= {'onclick' : 'this.form.submit();'}),
   #             choices=source_choices, initial="all")

