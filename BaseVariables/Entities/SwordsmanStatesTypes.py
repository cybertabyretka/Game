from Controllers.Entities.States.NPCs.Swordsman.SwordsmanIdleState import SwordsmanIdleState
from Controllers.Entities.States.NPCs.Swordsman.SwordsmanWalkState import SwordsmanWalkState
from Controllers.Entities.States.NPCs.Swordsman.SwordsmanAfterPunchState import SwordsmanAfterPunchState
from Controllers.Entities.States.NPCs.Swordsman.SwordsmanPunchState import SwordsmanPunchState
from Controllers.Entities.States.NPCs.Swordsman.SwordsmanDeathState import SwordsmanDeathState
from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState

from Constants.StatesNames import *


SWORDSMAN_STATES_TYPES: dict[str, type[NPCBaseState]] = {IDLE_STATE: SwordsmanIdleState,
                                                         WALK_STATE: SwordsmanWalkState,
                                                         AFTER_PUNCH_STATE: SwordsmanAfterPunchState,
                                                         PUNCH_STATE: SwordsmanPunchState,
                                                         DEATH_STATE: SwordsmanDeathState}
