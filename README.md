## Overview

This repo has been setup to serve companion content for the article [Bots Over Ball: Fantasy Football Automated](https://www.lambdasandlapdogs.com/blog/bots-over-ball-fantasy-football-automated), this repository provides a ready-to-import Tines story and a full set of Python scripts to handle roster management, player stats, and injury updates—no football knowledge required.

Included:

- **Tines Story**: A complete, ready-to-import Tines workflow for automating fantasy football roster management using the Yahoo Fantasy Football API.
- **Python Scripts**: Web scraping and data parsing tools to gather additional player stats, projected points, and injury reports to supplement Yahoo’s data.
- **ChatGPT Prompts**: Custom prompts designed to optimize rosters and suggest add/drop actions.

## How It Works

1. **Roster and Standings Retrieval**: Tines pulls your current roster, league standings, and relevant player data using the Yahoo Fantasy Football API.
2. **Optimization and Recommendations**: ChatGPT analyzes the roster, suggesting lineup changes and add/drop actions based on projected points, injury status, and bye weeks.
3. **Slack Notifications**: Tines sends roster recommendations to Slack, allowing you to monitor suggestions in real time.

## Getting Started

### Prerequisites

- **Python 3.9+** with required libraries installed (e.g., BeautifulSoup for web scraping)
- **Tines** account to build/import provided story
- **Yahoo Developer** account and OAuth credentials to access the Fantasy Football API
- **Slack Developer** account for API integration if Slack notifications are desired

## Repository Structure

- **prompts/**: Contains custom prompts for ChatGPT to optimize rosters and suggest add/drop actions.
- **scripts/**: Contains Python scripts for scraping player stats, projected points, and injury data.
- **tines/**: Includes a ready-to-import Tines story for roster management.

## License

This project is licensed under the MIT License.

---

Let me know if this hits the mark or if there are any additional details you’d like included!