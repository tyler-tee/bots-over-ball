Your task is to evaluate a Fantasy Football roster for this week’s matchup, recommend optimal swaps based on projections, injuries, and bye weeks, and output the updated full roster in XML format. Ensure that:
- All starting positions (e.g., QB, WR1, WR2, RB1, RB2, TE, W/R/T, K, DEF) are filled with players expected to play.
- Exactly **six players are designated as "BN"** (bench).
- Avoid any duplicate positions, ensuring only one player per position to prevent API errors.

### Starting Criteria:
1. **Projected Points Comparison**: For each position, if a benched player has a higher projected weekly point total than a starter, recommend a swap.
2. **Injury Status Exclusion**: Exclude any player from the starting lineup who has an injury status of "IR," "O," "NFI-R," or "SUS."
3. **Bye Week Exclusion**: Ensure no starting players are on a bye week. If a starting player has a bye, replace them with the highest-projected, active bench player at the same position.

### XML Output Requirements:
Generate XML for the entire roster, ensuring that each position is filled with one unique player. Here’s the template:

```xml
### XML_START ###
<?xml version="1.0"?>
<fantasy_content>
  <roster>
    <coverage_type>week</coverage_type>
    <week><<get_current_week.current_week>></week> 
    <players>
      <!-- Starting Positions -->
      <player>
        <player_key>{{player_key_qb}}</player_key>
        <position>QB</position>
      </player>
      <player>
        <player_key>{{player_key_wr1}}</player_key>
        <position>WR</position>
      </player>
      <player>
        <player_key>{{player_key_wr2}}</player_key>
        <position>WR</position>
      </player>
      <player>
        <player_key>{{player_key_rb1}}</player_key>
        <position>RB</position>
      </player>
      <player>
        <player_key>{{player_key_rb2}}</player_key>
        <position>RB</position>
      </player>
      <player>
        <player_key>{{player_key_te}}</player_key>
        <position>TE</position>
      </player>
      <player>
        <player_key>{{player_key_flex}}</player_key>
        <position>W/R/T</position>
      </player>
      <player>
        <player_key>{{player_key_k}}</player_key>
        <position>K</position>
      </player>
      <player>
        <player_key>{{player_key_def}}</player_key>
        <position>DEF</position>
      </player>

      <!-- Bench Positions (exactly 6 players) -->
      <player>
        <player_key>{{player_key_bench1}}</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>{{player_key_bench2}}</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>{{player_key_bench3}}</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>{{player_key_bench4}}</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>{{player_key_bench5}}</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>{{player_key_bench6}}</player_key>
        <position>BN</position>
      </player>
    </players>
  </roster>
</fantasy_content>
### XML_END ###
```

### Example XML Output
When generating the full roster, ensure each player has a unique position assignment to avoid API conflicts. The output would resemble:

```xml
### XML_START ###
<?xml version="1.0"?>
<fantasy_content>
  <roster>
    <coverage_type>week</coverage_type>
    <week>10</week>
    <players>
      <!-- Starting Positions -->
      <player>
        <player_key>449.p.30977</player_key>
        <position>QB</position>
      </player>
      <player>
        <player_key>449.p.33398</player_key>
        <position>WR</position>
      </player>
      <player>
        <player_key>449.p.31868</player_key>
        <position>WR</position>
      </player>
      <player>
        <player_key>449.p.41048</player_key>
        <position>RB</position>
      </player>
      <player>
        <player_key>449.p.33508</player_key>
        <position>RB</position>
      </player>
      <player>
        <player_key>449.p.40878</player_key>
        <position>TE</position>
      </player>
      <player>
        <player_key>449.p.29399</player_key>
        <position>W/R/T</position>
      </player>
      <player>
        <player_key>449.p.34344</player_key>
        <position>K</position>
      </player>
      <player>
        <player_key>449.p.100021</player_key>
        <position>DEF</position>
      </player>

      <!-- Bench Positions (exactly 6 players) -->
      <player>
        <player_key>449.p.32723</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>449.p.40126</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>449.p.40095</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>449.p.34104</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>449.p.28227</player_key>
        <position>BN</position>
      </player>
      <player>
        <player_key>449.p.22244</player_key>
        <position>BN</position>
      </player>
    </players>
  </roster>
</fantasy_content>
### XML_END ###
```


Current Week:
<<get_current_week.current_week>>

Current Roster:
<<map_projected_points>>