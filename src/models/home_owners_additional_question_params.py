from dataclasses import dataclass

@dataclass
class HomeOwnersAdditionalQuestionsParams:
    deadbolts: str = ""
    central_fire: str = ""
    central_burglar: str = ""
    deductible: str = ""
    roof_valuation_endt: str = ""
    additional_comments: str = ""