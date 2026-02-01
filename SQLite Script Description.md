# AthletaBase - Sports Data Architecture - 

A comprehensive SQLite-based relational database system designed to manage sports league operations, including teams, players, matches, sponsorships, medical staff, and referees.

## Overview

AthletaBase is a complete sports league management database that demonstrates professional database design principles, normalization, and relational data modeling. This project provides a fully functional backend system for tracking all aspects of a sports league's operations.

## Features

### Core Entities
- **Teams**: Manage team information, cities, and coaching staff
- **Players**: Track player details, contracts, positions, and team assignments
- **Matches**: Schedule and record match results, locations, and officials
- **Referees**: Maintain referee information and match assignments
- **Medical Staff**: Manage healthcare professionals assigned to teams
- **Sponsors**: Track sponsorship agreements and financial partnerships

### Key Capabilities
- Complete CRUD operations for all entities
- Relational integrity with foreign key constraints
- Junction tables for many-to-many relationships
- Performance-optimized with strategic indexes
- Automated timestamp tracking
- Data validation with CHECK constraints
- Comprehensive reporting and analytics queries
- CSV export functionality

## Database Schema

### Main Tables

#### Team
- `Team_ID` (Primary Key, Auto-increment)
- `Name` (Unique, Required)
- `City`
- `CoachID`
- `Created_At` (Auto-timestamp)

#### Player
- `PID` (Primary Key, Auto-increment)
- `Name` (Required)
- `Phone_No`
- `DOB` (Date of Birth)
- `Address`
- `Position` (Forward, Midfielder, Defender, Goalkeeper)
- `Contract_Start`
- `Contract_End`
- `Team_ID` (Foreign Key → Team)
- `Created_At` (Auto-timestamp)

#### Match
- `MID` (Primary Key, Auto-increment)
- `MDate` (Match Date, Required)
- `Location`
- `Referee_ID` (Foreign Key → Referee)
- `Home_Team_ID` (Foreign Key → Team)
- `Away_Team_ID` (Foreign Key → Team)
- `Home_Score` (Default: 0)
- `Away_Score` (Default: 0)
- `Status` ('Scheduled' or 'Completed')
- `Created_At` (Auto-timestamp)
- **Constraint**: `Home_Team_ID` ≠ `Away_Team_ID`

#### Medical_Staff
- `MedID` (Primary Key, Auto-increment)
- `Name` (Required)
- `Role` (Required)
- `Created_At` (Auto-timestamp)

#### Sponsor
- `SID` (Primary Key, Auto-increment)
- `Name` (Required)
- `Type`
- `Contact_Details`
- `Created_At` (Auto-timestamp)

#### Referee
- `RID` (Primary Key, Auto-increment)
- `Name` (Required)
- `Phone_No`
- `Created_At` (Auto-timestamp)

### Junction Tables (Many-to-Many Relationships)

#### Has_Medical_Staff
Links medical professionals to teams they serve.
- `MedID` (Foreign Key → Medical_Staff)
- `Team_ID` (Foreign Key → Team)
- `Assignment_Date`
- `Role_Description`
- **Primary Key**: (MedID, Team_ID)

#### Has_Sponsor
Tracks sponsorship agreements between sponsors and teams.
- `SID` (Foreign Key → Sponsor)
- `Team_ID` (Foreign Key → Team)
- `Sponsorship_Amount` (Decimal)
- `Start_Date`
- `End_Date`
- `Contract_Details`
- **Primary Key**: (SID, Team_ID)

#### Play
Records which teams participated in which matches.
- `Team_ID` (Foreign Key → Team)
- `MID` (Foreign Key → Match)
- `Team_Type` ('HOME' or 'AWAY')
- `Team_Score`
- **Primary Key**: (Team_ID, MID)

#### Have_Referee
Assigns referees to matches with their specific roles.
- `RID` (Foreign Key → Referee)
- `MID` (Foreign Key → Match)
- `Referee_Role` (e.g., 'Main Referee', 'Assistant Referee')
- **Primary Key**: (RID, MID)

## Getting Started

### Prerequisites
- Python 3.7+
- Required packages:
  ```bash
  pip install sqlite3 pandas
  ```

### Installation

1. **Clone or download the notebook**
   ```bash
   git clone <repository-url>
   ```

2. **Open in Google Colab**
   - Upload the `.ipynb` file to Google Colab
   - Or use the "Open in Colab" badge at the top of the notebook

3. **Run all cells**
   - Execute cells sequentially from top to bottom
   - The database will be created automatically

## Usage

### Database Creation
The notebook :
1. Creates the SQLite database (`sports_league.db`)
2. Sets up all tables with proper relationships
3. Creates performance indexes
4. Populates sample data

### Sample Data Included
- **8 Teams**: Thunder Hawks, Lightning Strikes, Storm Chasers, Fire Dragons, Ice Wolves, Wave Riders, Mountain Lions, Desert Eagles
- **15 Players**: Distributed across teams with various positions
- **8 Matches**: Mix of completed and scheduled matches
- **6 Referees**: With match assignments
- **6 Medical Staff**: Assigned to different teams
- **6 Sponsors**: With sponsorship contracts

### Running Queries

The notebook includes comprehensive analysis queries:

#### 1. Team Statistics
```python
# View team performance metrics
- Matches Played
- Wins, Losses, Draws
- Goals Scored & Conceded
```

#### 2. Player Roster
```python
# List all players by team and position
```

#### 3. Match Schedule & Results
```python
# View past results and upcoming matches
```

#### 4. Sponsorship Analysis
```python
# Track sponsorship revenue by team
```

#### 5. Medical Staff Assignments
```python
# See which medical professionals serve each team
```

#### 6. Referee Statistics
```python
# Analyze referee workload and roles
```

#### 7. Contract Expiration Tracking
```python
# Monitor upcoming player contract expirations
```

## Performance Optimization

### Indexes
Strategic indexes created for optimal query performance:
- `idx_player_team`: Fast player-team lookups
- `idx_player_position`: Quick position-based queries
- `idx_match_date`: Efficient date-range queries
- `idx_match_teams`: Optimized team match history
- `idx_match_referee`: Quick referee assignment lookups
- `idx_team_name`: Fast team name searches

## Key Queries & Reports

### 1. Team Profile Report
Comprehensive overview of a specific team including:
- Basic information (name, city)
- Player count
- Total sponsorship revenue
- Medical staff count

### 2. Position Distribution
Analyzes player distribution across positions with percentages.

### 3. Upcoming Matches
Lists all scheduled future matches with venues and officials.

### 4. Sponsorship Revenue Analysis
Calculates total sponsorship income per team, ranked by revenue.

## Database Design Principles

### Normalization
- **3NF Compliance**: Eliminates redundancy and ensures data integrity
- **Atomic Values**: Each field contains single, indivisible values
- **No Transitive Dependencies**: Proper separation of concerns

### Referential Integrity
- **Foreign Keys**: Enforce relationships between tables
- **Cascade Options**: Appropriate ON DELETE behaviors
  - `CASCADE`: For junction tables
  - `SET NULL`: For optional relationships

### Data Validation
- **NOT NULL Constraints**: Critical fields cannot be empty
- **UNIQUE Constraints**: Prevent duplicate team names
- **CHECK Constraints**: Validate data (e.g., home ≠ away team)
- **DEFAULT Values**: Automatic timestamps, initial scores

## Use Cases

This database architecture is suitable for:
- Sports league management systems
- Tournament organization platforms
- Player contract management
- Sponsorship tracking systems
- Match scheduling applications
- Team analytics dashboards
- Sports data warehousing
- Fantasy sports backends

## Customization

### Adding New Teams
```python
cursor.execute('''
    INSERT INTO Team (Name, City, CoachID)
    VALUES (?, ?, ?)
''', ('Team Name', 'City', coach_id))
```

### Recording Match Results
```python
cursor.execute('''
    UPDATE Match
    SET Home_Score = ?, Away_Score = ?, Status = 'Completed'
    WHERE MID = ?
''', (home_score, away_score, match_id))
```

### Adding Player Contracts
```python
cursor.execute('''
    INSERT INTO Player (Name, Position, Team_ID, Contract_Start, Contract_End)
    VALUES (?, ?, ?, ?, ?)
''', (name, position, team_id, start_date, end_date))
```

## Learning Outcomes

This project demonstrates:
- Relational database design
- SQL DDL (Data Definition Language)
- SQL DML (Data Manipulation Language)
- Complex JOIN operations
- Aggregate functions and GROUP BY
- Subqueries and CTEs
- Index optimization
- Data integrity constraints
- Python-SQLite integration
- Pandas for data analysis

## Data Integrity Features

- **Automatic Timestamps**: Created_At fields auto-populate
- **Referential Actions**: Proper cascade/set null on deletes
- **Unique Constraints**: Prevent duplicate critical data
- **Type Safety**: Proper data types for all fields
- **Range Validation**: Check constraints for logical data

## Sample Analytics

The notebook includes ready-to-run analytics:
1. **League Standings**: Ranked by wins and goals
2. **Top Scorers**: Teams with highest goal tallies
3. **Revenue Leaders**: Teams by sponsorship income
4. **Contract Alerts**: Players with expiring contracts
5. **Referee Workload**: Match assignments per official
6. **Team Rosters**: Complete player listings
7. **Position Analysis**: Squad composition breakdown

## Contributing

This is an educational project demonstrating database design concepts. Suggestions for improvements:
- Additional entity types (coaches, venues, leagues)
- More complex queries and views
- Stored procedures for common operations
- Trigger implementations
- Full-text search capabilities
- Multi-league support

## Author - Abirami Baskaran

Created as a demonstration of professional database architecture and SQL proficiency.

## Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Database Normalization Guide](https://en.wikipedia.org/wiki/Database_normalization)

## Support

For questions or issues with this notebook:
1. Review the inline comments in each code cell
2. Check the comprehensive query examples
3. Examine the schema diagram (can be generated using DB tools)

For questions and insights get in touch : 
Linkdln : https://www.linkedin.com/in/abiramihi/

---

**Note**: This is a demonstration database with sample data. For production use, additional security measures, user authentication, and data validation would be required.
