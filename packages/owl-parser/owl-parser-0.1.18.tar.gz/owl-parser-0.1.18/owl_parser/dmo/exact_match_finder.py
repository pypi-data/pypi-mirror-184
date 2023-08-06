#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Sliding Window Extraction for Candidate Synonym Swapping """


from pprint import pprint

from baseblock import EnvIO
from baseblock import BaseObject
from baseblock import Stopwatch

from owl_parser.dmo.exact import SlidingWindowBlacklist
from owl_parser.dmo.exact import SlidingWindowExtract
from owl_parser.dmo.exact import SlidingWindowLookup

from owl_parser.dto import d_candidate_synonym_blacklist


class ExactMatchFinder(BaseObject):
    """ Perform Sliding Window Extraction for Candidate Synonym Swapping """

    def __init__(self,
                 gram_size: int,
                 d_lookup: dict):
        """
        Created:
            8-Oct-2021
            craigtrim@gmail.com
            *   GRAFFL-CORE-0004
        Updated:
            20-Oct-2021
            craigtrim@gmail.com
            *   renamed from 'perform-sliding-window'
                GRAFFL-CORE-0077
        """
        BaseObject.__init__(self, __name__)
        self._d_lookup = d_lookup
        self._gram_size = gram_size

    def _process(self,
                 tokens: list) -> list:

        # if there are no valid synonyms or entities at this gram size level
        if self._gram_size not in self._d_lookup:
            return None  # ... then there is no point in proceeding any further

        candidates = SlidingWindowExtract(
            tokens=tokens,
            gram_size=self._gram_size).process()

        if not candidates or not len(candidates):
            return None

        if self._gram_size == 1:
            candidates = [x for x in candidates if len(
                [token for token in x if 'swaps' not in token])]

        if EnvIO.is_true('SLIDING_WINDOW_BLACKLIST'):  # optional step; defaults to False
            if self._gram_size in d_candidate_synonym_blacklist:
                blacklist = d_candidate_synonym_blacklist[self._gram_size]

                candidates = SlidingWindowBlacklist(
                    candidates=candidates,
                    blacklist=blacklist,
                    gram_size=self._gram_size).process()

                if not candidates or not len(candidates):
                    return None

        candidates = SlidingWindowLookup(
            candidates=candidates,
            gram_size=self._gram_size,
            d_runtime_kb=self._d_lookup).process()

        if not candidates or not len(candidates):
            return None

        return candidates

    def process(self,
                tokens: list) -> list:
        sw = Stopwatch()

        results = self._process(tokens)

        if self.isEnabledForInfo:

            def total_results() -> int:
                if results:
                    return len(results)
                return 0

            if self.isEnabledForInfo:
                self.logger.info('\n'.join([
                    'Sliding Window Completed',
                    f'\tGram Size: {self._gram_size}',
                    f'\tTotal Results: {total_results()}',
                    f'\tTotal Time: {str(sw)}']))

        return results
