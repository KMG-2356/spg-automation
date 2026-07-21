from dataclasses import dataclass

@dataclass
class DFapplicantInfoParams:
    insured_credit_history: str = ""
    Any_Arson_Fraud_convictions: str = ""
    Bankruptcy_Last_Year: str = ""
    Foreclosure_Last_5Years: str = ""
    AnyPast_Due_Child_Support: str = ""
    Repossessions_Last_3Years: str = ""
    Prior_Insuranceon_This_Account: str = ""
    Prior_CarrierName: str = ""
    Expiration_Date_of_Prior_Insurance: str = ""
    Prior_Policy_Number: str = ""
    Prior_Insurance_Premium: str = ""
    Risk_New_to_Agency: str = ""
    Lapse_30_Days: str = ""
    Terminate_at_Company_Request: str = ""
    Reason_for_Termination: str = ""
    Previous_WindHail_Dedductible: str = ""
                             