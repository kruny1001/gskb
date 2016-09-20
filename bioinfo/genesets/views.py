from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.forms.models import model_to_dict

from models import Genesets

# Construct verbosename/name pair
GenesetFields = []
GenesetFieldNames = []
for f in Genesets._meta.fields:
    GenesetFields.append((f.verbose_name, f.name))
    GenesetFieldNames.append(f.name)

# fields should be displayed without escaping on the single-geneset page
urlFields = ['detailsurl', 'pubmed'] 

# These fields should not be displayed on the single-geneset page
excludeFields = ['label']
def geneset(request):
    '''Handles requests for a particular geneset specified by the label
    GET parameter.
    '''

    # Safety checks to ensure safe use of GET
    if not (request.method == "GET" and len(request.GET) > 0 and 'label' in
        request.GET):
        raise Http404

    inLabel = request.GET['label']

    # Fetch DB object
    try:
        #g = Genesets.objects.filter(label=gs)
        g = Genesets.objects.get(label=inLabel)
    except Genesets.DoesNotExist:
        raise Http404

    if g.detailsurl:
        g.detailsurl = '<a href="' + g.detailsurl + '">' + g.detailsurl + \
                       '</a>'

    if g.pubmed:
        g.pubmed = r'<a href="http://www.ncbi.nlm.nih.gov/pubmed?term=' + \
                    g.pubmed + '">' + g.pubmed + '</a>'

    exportFields = []
    for f in GenesetFields:
        val = eval('g.%s' % (f[1],))
        if (not val) or \
            (f[1] in excludeFields): # Skip empty columns and some fields
            continue

        safe = True if f[1] in urlFields else False
        exportFields.append((f[0], val, safe))

    return render_to_response('genesets/geneset.html', locals())



# Provide the search interface. Always renders the search box at the top.
# If the user previously searched for something, we display that.

from django.db.models import Q
from genesets.forms import SearchForm

from unicodecsv import DictWriter
from django.core import serializers


def render_non_html(encoding,querySet):
    '''Renders non-html formats and returns an appropriate HttpResponse'''

    if encoding == 'csv':
        vals = querySet.values()
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = \
                'attachment; filename=genesets%d.csv' % len(vals)
        csvW = DictWriter(response,GenesetFieldNames)
        fieldsDict = {}
        for k in GenesetFieldNames:
            fieldsDict[k] = k
        csvW.writerow(fieldsDict)
        csvW.writerows(vals)
    elif encoding == 'xml':
        response = HttpResponse(mimetype='text/xml')
        response['Content-Disposition'] = \
                'attachment; filename=genesets%d.xml' % len(querySet)
        serializers.serialize("xml", querySet, stream=response)
    elif encoding == "json":
        response = HttpResponse(mimetype='application/json')
        response['Content-Disposition'] = \
                'attachment; filename=genesets%d.js' % len(querySet)
        serializers.serialize("json", querySet, stream=response)

    return response

def gsall(request):
    '''Displays all records. Form has the search component hidden and always
    instant-filters based on sources'''
    searched = True
    link_prepend = "../"
    show_all = True # Tell the template that we are displaying all records
    inSource = "all" # Default is to show all sources

    if request.method == "GET" and len(request.GET) > 0:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()

    # Because the user is viewing all records, no need for a text search field
    del form.fields['search']

    # Enable instant selection if the user changes the source selector
    # Only want to do this once there are results, since it wouldn't make sense
    # without them.
    form.fields['sources'].widget.attrs['onclick'] = 'this.form.submit();'

    results = Genesets.objects.all() # By default, user gets all records

    if form.is_valid():
        inSource = form.cleaned_data['sources']
        if inSource != 'all':
            results = Genesets.objects.filter(source=inSource)
        # If data requested in non-html formats
        encoding = form.cleaned_data['encoding']
        if encoding != 'html':
            return render_non_html(encoding, results)

    return render_to_response('genesets/search.html', locals())

def gssearch(request):
    '''Geneset search function'''

    if request.method == "GET" and len(request.GET) > 0:
        form = SearchForm(request.GET)
        if not form.is_valid():
            return render_to_response('genesets/search.html', locals())
    else:
        form = SearchForm()
        return render_to_response('genesets/search.html', locals())
    
    ### We have a valid form
    # See gsall
    form.fields['sources'].widget.attrs['onclick'] = 'this.form.submit();'

    search = form.cleaned_data['search']
    searched = True # Indicates that something was searched for (even "")
#    qset = (
#            Q(label__search=search) |
#            Q(firstauthor__search=search) |
#            Q(descriptionbrief__search=search) |
#            Q(genes__search=search) |
#            Q(genessym__search=search) |
#            Q(citation__search=search)
#        )
# This is the alternative version that doesn't depend on mysql's full text

    qset = Q() # Start with an empty query. Empty search means show everything
    for term in search.split():
        # whitespace-separated words are ANDed together
        qset &= (Q(label__icontains=term) |
                 Q(firstauthor__icontains=term) |
                 Q(descriptionbrief__icontains=term) |
                 Q(genes__icontains=term) |
                 Q(genessym__icontains=term) |
                 Q(citation__icontains=term))

    inSource = form.cleaned_data['sources']
    if inSource != 'all':
        qset = qset & Q(source=inSource)

    results = Genesets.objects.filter(qset).distinct()

    # If data requested in non-html formats, send to render_non_html()
    # The only exception to this is if there were no results
    encoding = form.cleaned_data['encoding']
    if encoding == 'html' or len(results) == 0:
        return render_to_response('genesets/search.html', locals())
    else:
        return render_non_html(encoding, results)

