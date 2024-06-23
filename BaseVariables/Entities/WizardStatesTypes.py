from Controllers.Entities.States.NPCs.Wizard.WizardIdleState import WizardIdleState
from Controllers.Entities.States.NPCs.Wizard.WizardWalkState import WizardWalkState
from Controllers.Entities.States.NPCs.Wizard.WizardAfterPunchState import WizardAfterPunchState
from Controllers.Entities.States.NPCs.Wizard.WizardPunchState import WizardPunchState
from Controllers.Entities.States.NPCs.Wizard.WizardDeathState import WizardDeathState
from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState

from Constants.StatesNames import *


WIZARD_STATES_TYPES: dict[str, type[NPCBaseState]] = {IDLE_STATE: WizardIdleState,
                                                      WALK_STATE: WizardWalkState,
                                                      AFTER_PUNCH_STATE: WizardAfterPunchState,
                                                      PUNCH_STATE: WizardPunchState,
                                                      DEATH_STATE: WizardDeathState}
