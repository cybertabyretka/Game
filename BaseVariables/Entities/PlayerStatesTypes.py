from Constants.StatesNames import *

from Controllers.Entities.States.Player.PlayerAfterPunchState import PlayerAfterPunchState
from Controllers.Entities.States.Player.PlayerPunchState import PlayerPunchState
from Controllers.Entities.States.Player.PlayerWalkState import PlayerWalkState
from Controllers.Entities.States.Player.PlayerShieldState import PlayerShieldState
from Controllers.Entities.States.Player.PlayerInventoryOpenState import PlayerInventoryOpenState
from Controllers.Entities.States.Player.PlayerStealState import PlayerStealState
from Controllers.Entities.States.Player.PlayerIdleState import PlayerIdleState


PLAYER_STATES_TYPES = {WALK_STATE: PlayerWalkState,
                       PUNCH_STATE: PlayerPunchState,
                       AFTER_PUNCH_STATE: PlayerAfterPunchState,
                       SHIELD_STATE: PlayerShieldState,
                       INVENTORY_OPEN_STATE: PlayerInventoryOpenState,
                       STEAL_STATE: PlayerStealState,
                       IDLE_STATE: PlayerIdleState}
