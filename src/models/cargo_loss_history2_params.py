from dataclasses import dataclass, field
from typing import List

@dataclass
class LossHistory2Record:
    details: str=""
    type_of_loss: str = ""
    loss_date: str = ""
    amount: str = ""

@dataclass
class SubjectivityRecord:
    subjectivity_text: str = ""

@dataclass
class CargoLossHistory2Params:
   any_losses_in_the_past3_years: str = ""
   any_unrepaired_damage_from_prior_losses: str = ""
   add_extra_subjectivities: str = ""   
   notes_about_the_insured: str = ""
   losses2: List[LossHistory2Record] = field(default_factory=list)
   subjectivity: List[SubjectivityRecord] = field(default_factory=list)



