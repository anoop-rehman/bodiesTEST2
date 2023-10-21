import numpy as np
from dm_control import viewer
from dm_control.locomotion import soccer as dm_soccer

# Define intuitive action mappings
ACTION_MAPPINGS = {
    "move_up": np.array([1.0, 0.0, 0.0]),
    "move_down": np.array([-1.0, 0.0, 0.0]),
    "turn_left": np.array([0.0, -1.0, 0.0]),
    "turn_right": np.array([0.0, 1.0, 0.0]),
    "shoot": np.array([0.0, 0.0, 1.0]),
    "no_action": np.array([0.0, 0.0, 0.0]),
}

def intuitive_to_action(intuitive_command):
    """Converts an intuitive command to its numerical action."""
    return ACTION_MAPPINGS.get(intuitive_command, ACTION_MAPPINGS["no_action"])

def get_relative_positions(physics):
    # Updated player names based on the printed body names
    player_names = ["home0/head_body", "home1/head_body", "away0/head_body", "away1/head_body"]
    ball_name = "soccer_ball/"

    # Extract positions
    player_positions = [physics.named.data.xpos[player][:2].copy() for player in player_names]  # Exclude z-coordinate
    ball_position = physics.named.data.xpos[ball_name][:2].copy()  # Exclude z-coordinate

    # If you want positions relative to the center of the field:
    center_of_field = np.array([0.0, 0.0])  # Adjust as necessary (excluding z-coordinate)
    relative_player_positions = [pos - center_of_field for pos in player_positions]
    relative_ball_position = ball_position - center_of_field

    # Determine ball possession for each player
    possession_threshold = 1.0  # Adjust this value based on your requirements
    player_possessions = [np.linalg.norm(pos - ball_position) < possession_threshold for pos in relative_player_positions]

    return relative_player_positions, relative_ball_position, player_possessions

# Instantiates a 2-vs-2 BOXHEAD soccer environment with episodes of 10 seconds
env = dm_soccer.load(team_size=2,
                     time_limit=10.0,
                     disable_walker_contacts=False,
                     enable_field_box=True,
                     terminate_on_goal=False,
                     walker_type=dm_soccer.WalkerType.BOXHEAD)

# Retrieves action_specs for all 4 players.
action_specs = env.action_spec()
print("\n", action_specs)

# Define a policy function to provide actions to the viewer
def policy(time_step, env=env):
    body_names = [env.physics.model.names[env.physics.model.name_bodyadr[i]:env.physics.model.name_bodyadr[i+1]].decode('utf-8').strip() for i in range(env.physics.model.nbody - 1)]

    print(body_names)
    actions = []
    intuitive_command = "move_up"  
    action = intuitive_to_action(intuitive_command)
    for _ in action_specs:
        actions.append(action)

    # Print relative positions and ball possession
    relative_player_positions, relative_ball_position, player_possessions = get_relative_positions(env.physics)
    print("Relative Player Positions:", relative_player_positions)
    print("Relative Ball Position:", relative_ball_position)
    print("Ball Possession:", player_possessions)

    return actions

# Launch the viewer with the environment and policy
viewer.launch(env, policy=policy)
