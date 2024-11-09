Your task is to evaluate the current Fantasy Football roster for this week’s matchup, considering both players held in the roster and available free agents. Recommend add/drop actions where an available player has better projected points, fewer injury risks, or fills gaps (e.g., due to bye weeks). Provide recommendations in the following structured array:

```json
[{"add_player_name": "{player_name}", "drop_player_name": "{player_name}", "rationale": ""}...]
```

Evaluation Criteria:
Projected Points Comparison: Identify available players with higher projected points than those on the current roster in similar positions. Recommend adding these players and dropping lower-projected, less valuable, or riskier roster players.
Injury Status Exclusion: Prioritize adding available players over roster players who are on "IR," "O," "NFI-R," or "SUS" injury statuses. Exclude these injured players from starting or bench roles.
Bye Week Replacement: For any roster player on a bye week, recommend an available player in the same position with the highest projected points.

#### Input Variables:
- **Current Week**: <<get_current_week.current_week>>
- **Current Roster**: <<map_projected_points>>
- **Available Players**: <<update_injury_status>>

