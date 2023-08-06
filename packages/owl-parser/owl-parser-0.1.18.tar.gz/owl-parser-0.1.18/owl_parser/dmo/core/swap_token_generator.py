#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate a Swapped Token """


from baseblock import BaseObject, Enforcer


class SwapTokenGenerator(BaseObject):
    """ Generate a Swapped Token """

    def __init__(self,
                 ontologies: list):
        """ Change Log

        Created:
            20-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'exact-match-swapper'
                GRAFFL-CORE-0077
        Updated:
            1-Feb-2022
            craigtrim@gmail.com
            *   pass 'ontologies' as list param
                https://github.com/grafflr/graffl-core/issues/135#issuecomment-1027464370
        Updated:
            27-May-2022
            craigtrim@gmail.com
            *   remove all params in place of 'find-ontology-data'
                https://github.com/grafflr/deepnlu/issues/13

        Args:
            ontologies (list): list of OWL models
        """
        BaseObject.__init__(self, __name__)
        self._ontologies = ontologies

    def process(self,
                normal: str,
                canon: str,
                ner: str,
                tokens: list,
                swap_type: str,
                confidence: float = 100.0) -> dict:

        Enforcer.is_str(normal)
        Enforcer.is_str(canon)
        Enforcer.is_optional_str(ner)
        Enforcer.is_list(tokens)
        Enforcer.is_optional_str(normal)

        if ner:
            ner = ner.upper()

        def get_ontologies() -> list:
            if type(self._ontologies) == list:
                return self._ontologies
            return [self._ontologies]

        return {
            'id': tokens[0]['id'],
            'x': tokens[0]['x'],
            'y': tokens[-1]['y'],
            'ner': ner,
            'text': ' '.join([x['text'].strip() for x in tokens]),
            'normal': normal,
            'swaps': {
                'tokens': tokens,
                'canon': canon,
                'type': swap_type,
                'ontologies': get_ontologies(),
                'confidence': confidence
            }
        }
