from Controllers.Entities.States.NPCs.WizardStates import *


WIZARD_STATES_TYPES: dict[str, type[NPCBaseState]] = {'idle_state': WizardIdleState,
                                                      'walk_state': WizardWalkState,
                                                      'after_punch_state': WizardAfterPunchState,
                                                      'punch_state': WizardPunchState,
                                                      'death_state': WizardDeathState}