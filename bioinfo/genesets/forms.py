from django import forms
from django.utils.safestring import mark_safe


# Options for sources from which to load.
# Note: empty source choices will allow for the downloading of empty
#       alternatively-formatted output (like CSV and xml). gssearch()
#       has logic to prevent this
source_choices = (('all','All'),
                  ('Literature','Literature'),
                  ('AraCyc','AraCyc'),
                  ('Computational','Computational'),
                  ('GO_BP','GO_BP'),
                  ('GO_CC','GO_CC'),
                  ('GO_MF','GO_MF'),
                  ('KEGG','KEGG'),
                  ('miRNA','miRNA'),
                  ('PO','PO'),
                  ('TF','TF'))

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
                             Examples (remove quotes when using): Gene names (like "WRKY" or "WRKY TUB5"),
                             keywords (like "cold"), or first authors (like
                             "Mueller")''')
    sources = forms.ChoiceField(required=True,
                widget = forms.RadioSelect(renderer=HorizontalRadioRenderer),
                choices=source_choices, initial="all")
    encoding = forms.ChoiceField(label='Format', choices=encoding_choices,
                                 initial='html')
    
   # sources = forms.ChoiceField(required=True,
   #             widget = forms.RadioSelect(renderer=HorizontalRadioRenderer,
   #             attrs= {'onclick' : 'this.form.submit();'}),
   #             choices=source_choices, initial="all")

