from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,render_to_response
from django.forms.models import model_to_dict

from models import Genesets,GenesetsTable

# Construct verbosename/name pair
GenesetFields = []
for f in Genesets._meta.fields:
    GenesetFields.append((f.verbose_name, f.name))

excludeFields = ['label']

def geneset(request, gs):
    '''Handles requests for a particular geneset specified by the gs
    parameter.
    '''
    try:
        #g = Genesets.objects.filter(label=gs)
        g = Genesets.objects.get(label=gs)
    except Genesets.DoesNotExist:
        raise Http404


#    g = Genesets.objects.get(label=gs)
#    if (g.count() == 0):
#        raise Http404

    if g.detailsurl:
        g.detailsurl = '<a href="' + g.detailsurl + '">Link</a>'

    if g.pubmed:
        g.pubmed = r'<a href="http://www.ncbi.nlm.nih.gov/pubmed?term=' + \
                    g.pubmed + '">' + g.pubmed + '</a>'

    exportFields = []
    for f in GenesetFields:
        val = eval('g.%s' % (f[1],))
        if (not val) or \
            (f[1] in excludeFields): # Skip empty columns and some fields
            continue
        exportFields.append((f[0], val))

    return render(request, 'genesets/geneset.html', locals())
