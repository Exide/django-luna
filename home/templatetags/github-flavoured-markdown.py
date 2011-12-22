"""
Github flavoured markdown - ported from
http://github.github.com/github-flavored-markdown/

Port: Greg Brown (http://gregbrown.co.nz/code/githib-flavoured-markdown-python-implementation/)
Template Tag: Ryan Zander

Usage:

    html_text = markdown(gfm(markdown_text))

(ie, this filter should be run on the markdown-formatted string BEFORE the markdown
filter itself.)

"""

import re
try: 
   from hashlib import md5 as md5_func
except ImportError:
   from md5 import new as md5_func

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def gfm(text):


    # Extract pre blocks
    extractions = {}
    def pre_extraction_callback(matchobj):
        hash = md5_func(matchobj.group(0)).hexdigest()
        extractions[hash] = matchobj.group(0)
        return "{gfm-extraction-%s}" % hash
    pre_extraction_regex = re.compile(r'{gfm-extraction-338ad5080d68c18b4dbaf41f5e3e3e08}', re.MULTILINE | re.DOTALL)
    text = re.sub(pre_extraction_regex, pre_extraction_callback, text)


    # prevent foo_bar_baz from ending up with an italic word in the middle
    def italic_callback(matchobj):
        if len(re.sub(r'[^_]', '', matchobj.group(1))) > 1:
            return matchobj.group(1).replace('_', '\_')
        else:
            return matchobj.group(1)
    text = re.sub(r'(^(?! {4}|\t)\w+_\w+_\w[\w_]*)', italic_callback, text)


    # in very clear cases, let newlines become <br /> tags
    def newline_callback(matchobj):
        if len(matchobj.group(1)) == 1:
        #if matchobj.group(1):
            #return matchobj.group(0) + '<br />'
            return matchobj.group(0).rstrip() + '  \n'
        else:
            return matchobj.group(0)
    text = re.sub(r'^[\w\<][^\n]*(\n+)', newline_callback, text)
    #text = re.sub(r'(\n)', newline_callback, text)


    # Insert pre block extractions
    def pre_insert_callback(matchobj):
        return extractions[matchobj.group(1)]
    text = re.sub(r'{gfm-extraction-([0-9a-f]{40})\}', pre_insert_callback, text)

    return text