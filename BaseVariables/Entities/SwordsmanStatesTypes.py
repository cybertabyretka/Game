from Controllers.Entities.States.NPCs.SwordsmanStates import *
from Controllers.Entities.States.NPCs.NPCsBaseStates import NPCBaseState


SWORDSMAN_STATES_TYPES: dict[str, type[NPCBaseState]] = {'idle_state': SwordsmanIdleState,
                                                         'walk_state': SwordsmanWalkState,
                                                         'after_punch_state': SwordsmanAfterPunchState,
                                                         'punch_state': SwordsmanPunchState,
                                                         'death_state': SwordsmanDeathState}
