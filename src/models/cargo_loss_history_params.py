from dataclasses import dataclass

@dataclass
class CargoAdditionalInformationParams:
   any_losses_in_the_past3_years: str = ""
   any_unrepaired_damage_from_prior_losses: str = ""
   loss_year: str = ""
   premium_at_time_of_loss: str = ""
   type_of_loss: str = ""
   loss_description: str = ""
   amount_paid: str = ""
   amount_outstanding: str = ""

