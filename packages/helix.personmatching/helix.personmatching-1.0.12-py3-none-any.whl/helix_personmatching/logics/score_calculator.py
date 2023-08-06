from typing import List, Optional

from helix_personmatching.logics.match_score_without_threshold import (
    MatchScoreWithoutThreshold,
)
from helix_personmatching.logics.rule_score import RuleScore
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.rule import Rule


class ScoreCalculator:
    @staticmethod
    def initialize_score(rules: List[Rule]) -> None:
        pass

    @staticmethod
    def calculate_total_score(
        rules: List[Rule],
        source: ScoringInput,
        target: ScoringInput,
        average_score_boost: Optional[float],
    ) -> MatchScoreWithoutThreshold:
        """
        Runs matching on two records: source and target


        :param rules:
        :param source:
        :param target:
        :param average_score_boost:
        :return: match score
        """
        match_results: List[RuleScore] = ScoreCalculator.calculate_score(
            rules=rules, source=source, target=target
        )
        if len(match_results) == 0:
            return MatchScoreWithoutThreshold(
                id_source=source.id_,
                id_target=target.id_,
                rule_scores=match_results,
                total_score=0.0,
                average_boost=None,
                average_score=0.0,
            )
        # Get the average match score as "final score" result
        # AND we're not penalizing the total match score,
        #  by excluding those rules that have 0 match scores when calculating the final match score,
        #  meaning the required data attributes/fields in the rule are not available or absent.
        final_score: float = 0

        sum_of_scores: float = 0
        rule_count: int = 0

        for match_result in match_results:
            # the score is uniqueness probability
            # pick the highest probability
            if match_result.rule_score > final_score:
                final_score = match_result.rule_score
            sum_of_scores += match_result.rule_score
            rule_count += 1
            if match_result.rule_boost is not None:
                final_score += match_result.rule_boost

        score_average_boost: Optional[float] = None
        score_average: float = 0
        # add a boost for average score
        if average_score_boost is not None:
            score_average = sum_of_scores / rule_count
            score_average_boost = score_average * average_score_boost
            if final_score + score_average_boost >= 1.0:
                # scale the boost so we don't go over 1.0
                diff = 1.0 - final_score
                max_average_score_boost = 1 * average_score_boost
                score_average_boost = (
                    score_average
                    * (average_score_boost / max_average_score_boost)
                    * diff
                )
            final_score += score_average_boost

        # cap total score at 1.0
        final_score = 1.0 if final_score > 1.0 else final_score

        return MatchScoreWithoutThreshold(
            id_source=source.id_,
            id_target=target.id_,
            rule_scores=match_results,
            total_score=final_score,
            average_boost=score_average_boost,
            average_score=score_average,
        )

    @staticmethod
    def get_number_of_rules_with_present_attributes(results: List[RuleScore]) -> int:
        number_of_rules_with_present_attributes: int = sum(
            map(
                lambda result: any(
                    list(
                        filter(
                            lambda rule_attribute_score: getattr(
                                rule_attribute_score, "present"
                            )
                            is True,
                            result.attribute_scores,
                        )
                    )
                )
                is True,
                results,
            )
        )
        number_of_rules_with_present_attributes = (
            1
            if number_of_rules_with_present_attributes == 0
            else number_of_rules_with_present_attributes
        )

        return number_of_rules_with_present_attributes

    @staticmethod
    def calculate_score(
        rules: List[Rule], source: ScoringInput, target: ScoringInput
    ) -> List[RuleScore]:
        """
        Calculate matching scores for ALL rules between FHIR Person-Person, or Person-Patient, or Person/Patient-AppUser
        :param rules: generated rules by RulesGenerator
        :param source: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :param target: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :return: list of dictionary for rules score results for all rules
        """

        rules_score_results: List[RuleScore] = []

        for rule in rules:
            rule_score_result: Optional[
                RuleScore
            ] = ScoreCalculator.calculate_score_for_rule(rule, source, target)
            if rule_score_result:
                rules_score_results.append(rule_score_result)

        return rules_score_results

    @staticmethod
    def calculate_score_for_rule(
        rule: Rule, source: ScoringInput, target: ScoringInput
    ) -> Optional[RuleScore]:
        return rule.score(source=source, target=target)
