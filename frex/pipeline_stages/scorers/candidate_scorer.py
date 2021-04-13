from abc import abstractmethod
from typing import Tuple, Generator, Any
from frex.models import Explanation, Candidate
from frex.pipeline_stages import PipelineStage


class CandidateScorer(PipelineStage):
    """
    CandidateScorer is a scoring pipeline stage that applies some score to candidates.
    """

    def __init__(self, *, scoring_explanation: Explanation, **kwargs):
        self.scoring_explanation = scoring_explanation

    @abstractmethod
    def score(self, *, candidate: Candidate) -> float:
        """
        Score a candidate

        :param candidate: A domain-specific candidate
        :return: Some score applied to the candidate based on the implemented scoring function.
        """
        pass

    def __call__(
        self, *, candidates: Generator[Candidate, None, None], context: Any
    ) -> Generator[Candidate, None, None]:
        for candidate in candidates:
            candidate.applied_explanations.append(self.scoring_explanation)
            candidate.applied_scores.append(self.score(candidate=candidate))
            yield candidate
