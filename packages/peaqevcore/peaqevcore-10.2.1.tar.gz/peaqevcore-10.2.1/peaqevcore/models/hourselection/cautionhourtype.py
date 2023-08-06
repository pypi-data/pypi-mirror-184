from enum import Enum

class CautionHourType(Enum):
    SUAVE = "Suave"
    INTERMEDIATE = "Intermediate"
    AGGRESSIVE = "Aggressive"

    @staticmethod
    def get_num_value(type_state):
        values = {
            CautionHourType.SUAVE.value: 0.75,
            CautionHourType.INTERMEDIATE.value: 0.5,
            CautionHourType.AGGRESSIVE.value: 0.4
            }

        if type_state in CautionHourType:
            tt = type_state.value
        else:
            tt = type_state
        
        return values[tt]



        