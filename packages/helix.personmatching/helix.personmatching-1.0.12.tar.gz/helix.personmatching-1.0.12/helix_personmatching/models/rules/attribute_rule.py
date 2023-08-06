from typing import List, Optional, Any

from rapidfuzz import distance

from helix_personmatching.logics.rule_attribute_score import RuleAttributeScore
from helix_personmatching.logics.rule_score import RuleScore
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.attribute_entry import AttributeEntry
from helix_personmatching.models.rule import Rule
from helix_personmatching.models.rules.RuleWeight import RuleWeight


class AttributeRule(Rule):
    def __init__(
        self,
        *,
        name: str,
        description: str,
        number: int,
        attributes: List[AttributeEntry],
        weight: RuleWeight
    ) -> None:
        super().__init__(
            name=name, description=description, number=number, weight=weight
        )
        self.attributes: List[AttributeEntry] = attributes

    def score(self, source: ScoringInput, target: ScoringInput) -> Optional[RuleScore]:
        """
        Calculate a matching score for one rule between FHIR Person-Person, or Person-Patient, or Person/Patient-AppUser


        :param source: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :param target: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :return: Dictionary of 1 rule score result
        """

        id_data_source: Optional[Any] = source.id_
        id_data_target: Optional[Any] = target.id_
        if not (id_data_source and id_data_target):
            return None

        rule_attribute_scores: List[RuleAttributeScore] = []
        score_avg: float = 0.0
        for attribute in self.attributes:
            rule_attribute_score: RuleAttributeScore = RuleAttributeScore(
                attribute=attribute, score=0.0, present=False, source=None, target=None
            )
            val_source: Optional[str] = getattr(source, attribute.name)
            val_target: Optional[str] = getattr(target, attribute.name)

            if val_source and val_target:
                rule_attribute_score.present = True

                # calculate exact string match on "trimmed lower" string values
                # returns a number between 0 and 1
                score_for_attribute = AttributeRule.calculate_string_match(
                    attribute, val_source, val_target
                )
                score_avg += score_for_attribute

                rule_attribute_score.score = score_for_attribute
                rule_attribute_score.source = val_source
                rule_attribute_score.target = val_target
            elif not val_source or not val_target:
                rule_attribute_score.score = self.weight.missing
                score_avg += self.weight.missing

            rule_attribute_scores.append(rule_attribute_score)

        score_avg /= len(self.attributes)

        my_score = (
            self.weight.exact_match
            if score_avg == 1.0
            else (score_avg * self.weight.partial_match)
        )

        rule_score: RuleScore = RuleScore(
            id_source=str(id_data_source),
            id_target=str(id_data_target),
            rule_name=self.name,
            rule_description=self.description,
            rule_score=my_score,
            rule_unweighted_score=score_avg,
            rule_weight=self.weight,
            attribute_scores=rule_attribute_scores,
        )

        return rule_score

    @staticmethod
    def calculate_string_match(
        attribute: AttributeEntry, val_source: Optional[str], val_target: Optional[str]
    ) -> float:
        """
        Returns a score from 0 to 1 where 1 is an exact match


        :param attribute:
        :param val_source:
        :param val_target:
        :return:
        """
        val_source_cleansed: str = str(val_source).strip().lower()
        val_target_cleansed: str = str(val_target).strip().lower()

        if attribute.exact_only:
            if val_source_cleansed == val_target_cleansed:
                return 1.0
            else:
                return 0.0

        score_for_attribute = distance.Levenshtein.normalized_similarity(
            val_source_cleansed,
            val_target_cleansed,
            # (give more weight to substitution since that is more typical to press a wrong key)
            weights=(1, 1, 2),  # insert, deletion, substitution
            score_cutoff=0.7,  # usually no more than two character changes
        )

        return score_for_attribute

    @staticmethod
    # In case for Considering ONLY available 'present' attributes in both source and target data.
    # i.e. Do not penalize the total rule average score by not available attributes.
    def get_total_number_of_available_attributes(
        rule_attribute_scores: List[RuleAttributeScore],
    ) -> int:
        total_number_of_available_attributes: int = sum(
            map(
                lambda x: x.present is True
                and x.source is not None
                and x.target is not None,
                rule_attribute_scores,
            )
        )
        return (
            1
            if total_number_of_available_attributes == 0
            else total_number_of_available_attributes
        )
