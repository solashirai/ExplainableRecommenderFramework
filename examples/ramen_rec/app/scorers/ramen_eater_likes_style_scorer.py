from frex.pipeline_stages.scorers import CandidateBoolScorer
from examples.ramen_rec.app.models import RamenEaterContext
from examples.ramen_rec.app.models import RamenCandidate
from typing import Tuple


class RamenEaterLikesStyleScorer(CandidateBoolScorer):
    def score(self, *, candidate: RamenCandidate) -> Tuple[bool, float]:
        if (
            candidate.context.ramen_eater_profile.likes_ramen_style
            == candidate.domain_object.style
        ):
            return True, 1.1
        else:
            return False, 0
