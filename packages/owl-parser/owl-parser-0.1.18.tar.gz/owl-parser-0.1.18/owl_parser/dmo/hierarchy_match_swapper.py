#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Synonym Swapping with Hierarchal Matches """


import itertools

from baseblock import BaseObject, Enforcer, Stopwatch

from owl_finder.multiquery.bp import FindOntologyData
from owl_parser.dmo import SwapTokenGenerator


class HierarchyMatchSwapper(BaseObject):
    """ Perform Synonym Swapping with Hierarchal Matches """

    def __init__(self,
                 find_ontology_data: FindOntologyData):
        """ Change Log

        Created:
            14-Feb-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/graffl-core/issues/188
        Updated:
            26-May-2022
            craigtrim@gmail.com
            *   treat 'ontologies' param as a list
                https://github.com/grafflr/deepnlu/issues/7
        Updated:
            27-May-2022
            craigtrim@gmail.com
            *   remove 'ontologies' and integrate 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            find_ontology_data (FindOntologyData): an instantiation of this object
        """
        BaseObject.__init__(self, __name__)
        self._exists = find_ontology_data.entity_exists
        self._create_swap = SwapTokenGenerator(
            find_ontology_data.ontologies()).process

    @staticmethod
    # TODO: baseblock >= 0.1.34
    def _cartesian(matches: list) -> list:
        """
        Purpose:
            Find a list of candidate token sequences within the normalized_input_text
        Time per Call:
            0.5ms < x 1.0ms
        :param matches:
            a list of 1..* tokens forming a match pattern
        :return:
            a list of possible token sequences
        """
        cartesian = []
        for element in itertools.product(*matches):
            cartesian.append(element)

        return cartesian

    def _surface_forms(self,
                       candidates: list) -> list:
        matches = []
        for token in candidates:

            def surface_forms() -> list:
                s = {token['normal']}

                if 'ancestors' in token:
                    [s.add(x) for x in token['ancestors']]

                if 'descendants' in token:
                    [s.add(x) for x in token['descendants']]

                if 'swaps' in token:
                    children = token['swaps']['tokens']

                    for child in [x for x in children
                                  if 'descendants' in x]:
                        [s.add(x) for x in child['descendants']]

                    for child in [x for x in children
                                  if 'ancestors' in x]:
                        [s.add(x) for x in child['ancestors']]

                return sorted(s)

            matches.append(surface_forms())

        return matches

    def _perform_swap(self,
                      tokens: list,
                      gram_size: int,
                      match_text: str,
                      candidates: list) -> list:

        def ner() -> str:
            if 'ner' in candidates[0]:
                return candidates[0]['ner']
            return candidates[0]['ent']

        d_swap = self._create_swap(normal=match_text,
                                   canon=match_text,
                                   ner=ner(),
                                   tokens=candidates,
                                   swap_type='hierarchy',
                                   confidence=75.0)

        def prior_tokens() -> list:
            results = []
            for token in tokens:
                if token['id'] != candidates[0]['id']:
                    results.append(token)
                else:
                    return results
            raise ValueError

        def post_tokens() -> list:
            results = []

            is_post = False
            for token in tokens:
                if is_post:
                    results.append(token)
                if token['id'] == candidates[-1]['id']:
                    is_post = True

            return results

        normalized = prior_tokens()
        normalized.append(d_swap)
        [normalized.append(x) for x in post_tokens()]

        return normalized

    def _process(self,
                 tokens: list,
                 gram_size: int,
                 list_of_candidates: list) -> list:

        for candidates in list_of_candidates:

            matches = self._surface_forms(candidates)
            if not matches or not len(matches):
                continue

            for match in self._cartesian(matches):
                match_text = '_'.join(match).strip().lower()
                if self._exists(match_text):
                    return self._perform_swap(tokens=tokens,
                                              gram_size=gram_size,
                                              match_text=match_text,
                                              candidates=candidates)

    def process(self,
                tokens: list,
                gram_size: int,
                list_of_candidates: list) -> list:

        if self.isEnabledForDebug:
            Enforcer.is_list(list_of_candidates)

        sw = Stopwatch()

        swaps = self._process(
            tokens=tokens,
            gram_size=gram_size,
            list_of_candidates=list_of_candidates)

        self.logger.info('\n'.join([
            'Hierarchy Match Swapping Completed',
            f'\tTotal Time: {str(sw)}']))

        return swaps
