import enum
from typing import Any, NamedTuple


class NomogramColumnName(NamedTuple):
    MSKCC: str
    CAPRA: str = "CAPRA Score"


class OutcomeDataFrameInformation(NamedTuple):
    outcome_column_name_in_dataframe: str
    value_of_negative_outcome: Any
    value_of_positive_outcome: Any
    nomograms: NomogramColumnName


LYMPH_NODE_CORES_INFO = OutcomeDataFrameInformation(
    outcome_column_name_in_dataframe="pN",
    value_of_negative_outcome="pN0",
    value_of_positive_outcome="pN1",
    nomograms=NomogramColumnName(
        MSKCC="Lymph Node Involvement (Cores)"
    )
)

BCR_5YEARS_INFO = OutcomeDataFrameInformation(
    outcome_column_name_in_dataframe="Récurrence 5 ans (60 mois) oui = 1 non =0",
    value_of_negative_outcome=0,
    value_of_positive_outcome=1,
    nomograms=NomogramColumnName(
        MSKCC="Preoperative BCR (Cores)_5_years"
    )
)


class Outcomes(enum.Enum):
    LYMPH_NODE_CORES = LYMPH_NODE_CORES_INFO
    BCR_5YEARS = BCR_5YEARS_INFO
