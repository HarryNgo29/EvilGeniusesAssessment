from ProcessGameState import ProcessGameState

# Example usage
game_state = ProcessGameState("game_state_frame_data.parquet")

# Question 1: Is entering via the light blue boundary a common strategy used by Team2 on the T side?
common_strategy = game_state.common_strategy_light_blue_boundary('Team2', 'T')
print("Entering via light blue boundary strategy usage:", common_strategy)

# Question 2: What is the average timer that Team2 on T side enters "BombsiteB" with at least 2 rifles or SMGs?
average_timer = game_state.average_entry_timer('Team2', 'T', 'BombsiteB', ['rifle', 'SMG'])
print("Average entry timer for Team2 on T side with rifles or SMGs:", average_timer)

# Question 3: Analyze Team2's CT side within "BombsiteB" and identify potential waiting areas (heatmap, etc.)
# Perform the necessary analysis and visualization