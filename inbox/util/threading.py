# -*- coding: utf-8 -*-
import re


def cleanup_subject(subject_str):
    """Clean-up a message subject-line.
    For instance, 'Re: Re: Re: Birthday party' becomes 'Birthday party'"""
    if subject_str is None:
        return ''
    cleanup_regexp = "^((Re:|RE:|fwd:|FWD:)\s*)+"
    return re.sub(cleanup_regexp, "", subject_str)
