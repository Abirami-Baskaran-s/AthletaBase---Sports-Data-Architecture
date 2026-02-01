# AthletaBase – Sports Data Architecture
## Relational Database Design & SQL Implementation

A centralized SQL-based relational database system designed to manage the complete data operations of a professional sports league. AthletaBase organizes teams, players, matches, staff, medical personnel, and sponsorship data into a single structured system that ensures accuracy, consistency, and efficient reporting.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Solution Architecture](#solution-architecture)
- [Database Schema](#database-schema)
- [Implementation](#implementation)
- [Features & Capabilities](#features--capabilities)
- [Data Analytics & Reporting](#data-analytics--reporting)
- [System Advantages](#system-advantages)
- [Technical Specifications](#technical-specifications)
- [Usage Examples](#usage-examples)
- [Future Enhancements](#future-enhancements)
- [Key Takeaways](#key-takeaways)
- [License](#license)

---

## Project Overview

AthletaBase replaces fragmented spreadsheets and manual records with a reliable relational database that ensures data integrity, prevents errors, and enables powerful analytics. The system is built around a normalized schema that models real-world sports league operations.

### Key Highlights

- **Comprehensive Data Management**: Handles all aspects of league operations from player contracts to match scheduling
- **Enforced Data Integrity**: Foreign key constraints prevent invalid data entry
- **Scalable Architecture**: Designed to grow with organizational needs
- **Advanced Analytics**: Complex queries provide actionable insights
- **Industry-Standard SQL**: Built using SQLite with portable, standardized code

---

## Problem Statement

Sports organizations often face critical data management challenges:

- **Fragmented Data**: Critical information scattered across multiple spreadsheets and manual records
- **Duplicate Entries**: Same data stored in multiple locations leading to inconsistencies
- **Data Integrity Issues**: Players assigned to non-existent teams, invalid match data, orphaned records
- **Slow Reporting**: Manual data compilation is time-consuming and error-prone
- **Inconsistent Naming**: No standardization across different data sources
- **Missing Relationships**: No enforced connections between related data entities

These issues result in operational inefficiencies, inaccurate reporting, and poor decision-making capabilities.

---

## Solution Architecture

AthletaBase solves these problems through strong relational database design:

### Core Design Principles

1. **Centralized Data Hub**: Single source of truth for all league information
2. **Normalized Structure**: Third Normal Form (3NF) reduces redundancy
3. **Relationship Enforcement**: Foreign keys maintain referential integrity
4. **Constraint Validation**: CHECK constraints prevent invalid data
5. **Automated Tracking**: Timestamps and auto-increment keys
6. **Cascading Actions**: Proper handling of related data on updates/deletes

### Entity-Relationship Model

The system is built around the **Team** entity as the central hub, connecting:
- Athletic talent (Players)
- Administrative staff (Coaches)
- Medical support (Medical Staff)
- Financial partnerships (Sponsors)
- Competitive events (Matches)
- Match officials (Referees)

---

## Database Schema

### Core Entities

#### 1. Team
**Purpose**: Central entity representing sports teams in the league

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| Team_ID | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique team identifier |
| Name | VARCHAR(100) | NOT NULL, UNIQUE | Team name |
| City | VARCHAR(100) | | Home city |
| CoachID | INTEGER | | Coach identifier |
| Created_At | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

**Relationships**:
- One-to-Many with Players
- One-to-Many with Medical Staff
- One-to-Many with Sponsors
- Many-to-Many with Matches

#### 2. Player
**Purpose**: Tracks individual athletes and their team assignments

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| PID | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique player identifier |
| Name | VARCHAR(100) | NOT NULL | Player name (composite: First, Middle, Last) |
| Phone_No | VARCHAR(20) | | Contact number |
| DOB | DATE | | Date of birth |
| Address | TEXT | | Residential address |
| Position | VARCHAR(50) | | Field position (Forward, Midfielder, Defender, Goalkeeper) |
| Contract_Start | DATE | | Contract start date |
| Contract_End | DATE | | Contract expiration date |
| Team_ID | INTEGER | FOREIGN KEY → Team(Team_ID) | Current team assignment |
| Created_At | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

**Relationship**: Many-to-One with Team (1:M)
- Each player belongs to exactly one team
- Teams maintain multiple players

#### 3. Match
**Purpose**: Represents competitive events between teams

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| MID | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique match identifier |
| MDate | DATE | NOT NULL | Match date |
| Location | VARCHAR(200) | | Venue location |
| Referee_ID | INTEGER | FOREIGN KEY → Referee(RID) | Assigned referee |
| Home_Team_ID | INTEGER | FOREIGN KEY → Team(Team_ID) | Home team |
| Away_Team_ID | INTEGER | FOREIGN KEY → Team(Team_ID) | Away team |
| Home_Score | INTEGER | DEFAULT 0 | Home team score |
| Away_Score | INTEGER | DEFAULT 0 | Away team score |
| Status | VARCHAR(20) | DEFAULT 'Scheduled' | Match status |
| Created_At | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

**Constraints**:
- CHECK: Home_Team_ID ≠ Away_Team_ID (prevents team playing itself)

**Relationships**:
- One-to-One with Referee (1:1) - Strict assignment
- Many-to-Many with Teams through Play junction table

#### 4. Referee
**Purpose**: Tracks match officials

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| RID | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique referee identifier |
| Name | VARCHAR(100) | NOT NULL | Referee name |
| Phone_No | VARCHAR(20) | | Contact number |
| Created_At | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

**Relationship**: One-to-One with Match (1:1)
- Each match has exactly one primary referee
- Each referee is assigned to specific matches

#### 5. Medical_Staff
**Purpose**: Manages healthcare professionals

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| MedID | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique medical staff identifier |
| Name | VARCHAR(100) | NOT NULL | Staff member name |
| Role | VARCHAR(50) | NOT NULL | Medical role (Physician, Physiotherapist, etc.) |
| Created_At | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

**Relationship**: One-to-Many with Team (1:M)
- Teams employ multiple medical staff
- Each staff member dedicated to one primary team

#### 6. Sponsor
**Purpose**: Tracks financial and commercial partnerships

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| SID | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique sponsor identifier |
| Name | VARCHAR(100) | NOT NULL | Sponsor name |
| Type | VARCHAR(50) | | Sponsor category |
| Contact_Details | TEXT | | Contact information |
| Created_At | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

**Relationship**: One-to-Many with Team (1:M)
- Teams can have multiple sponsors (Multiple-Sponsorship model)
- Each sponsor has primary team partnership

---

### Junction Tables (Many-to-Many Relationships)

#### Has_Medical_Staff
**Purpose**: Links medical professionals to teams

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| MedID | INTEGER | PRIMARY KEY, FOREIGN KEY → Medical_Staff(MedID) | Medical staff member |
| Team_ID | INTEGER | PRIMARY KEY, FOREIGN KEY → Team(Team_ID) | Assigned team |
| Assignment_Date | DATE | DEFAULT CURRENT_DATE | Assignment start date |
| Role_Description | TEXT | | Specific responsibilities |

**Composite Primary Key**: (MedID, Team_ID)

#### Has_Sponsor
**Purpose**: Tracks sponsorship agreements

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| SID | INTEGER | PRIMARY KEY, FOREIGN KEY → Sponsor(SID) | Sponsor company |
| Team_ID | INTEGER | PRIMARY KEY, FOREIGN KEY → Team(Team_ID) | Sponsored team |
| Sponsorship_Amount | DECIMAL(15, 2) | | Contract value |
| Start_Date | DATE | | Agreement start date |
| End_Date | DATE | | Agreement end date |
| Contract_Details | TEXT | | Agreement terms |

**Composite Primary Key**: (SID, Team_ID)

#### Play
**Purpose**: Records team participation in matches

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| Team_ID | INTEGER | PRIMARY KEY, FOREIGN KEY → Team(Team_ID) | Participating team |
| MID | INTEGER | PRIMARY KEY, FOREIGN KEY → Match(MID) | Match event |
| Team_Type | VARCHAR(10) | CHECK IN ('HOME', 'AWAY') | Home or away designation |
| Team_Score | INTEGER | DEFAULT 0 | Final score |

**Composite Primary Key**: (Team_ID, MID)

#### Have_Referee
**Purpose**: Assigns referees to matches with roles

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| RID | INTEGER | PRIMARY KEY, FOREIGN KEY → Referee(RID) | Referee assigned |
| MID | INTEGER | PRIMARY KEY, FOREIGN KEY → Match(MID) | Match assigned |
| Referee_Role | VARCHAR(50) | DEFAULT 'Main Referee' | Referee responsibility |

**Composite Primary Key**: (RID, MID)

---

## Implementation

### Database Technology
- **DBMS**: SQLite 3
- **Language**: SQL (DDL, DML, DQL)
- **Integration**: Python with sqlite3 module
- **Analysis**: Pandas for data manipulation and reporting

### Data Integrity Mechanisms

#### Primary Keys (PK)
- Auto-incrementing integer IDs for all main entities
- Ensures unique record identification
- Enables efficient indexing and joins

#### Foreign Keys (FK)
- Enforce referential integrity across tables
- Prevent orphaned records
- Create "web" of connectivity for complex queries

Example: TeamID in Player table ensures every player belongs to a valid team

#### Cascading Rules
- **ON DELETE CASCADE**: Junction tables automatically remove relationships
- **ON DELETE SET NULL**: Optional relationships preserve data integrity
- **ON DELETE RESTRICT**: Prevents deletion of referenced records

#### Check Constraints
- Position validation in Player table
- Team_Type validation in Play table ('HOME' or 'AWAY')
- Home_Team_ID ≠ Away_Team_ID in Match table

#### Normalization (3NF)
- **1NF**: Atomic values, no repeating groups
- **2NF**: No partial dependencies on composite keys
- **3NF**: No transitive dependencies
- Result: Minimal redundancy, maximum consistency

### Performance Optimization

#### Strategic Indexing
```sql
CREATE INDEX idx_player_team ON Player(Team_ID);
CREATE INDEX idx_player_position ON Player(Position);
CREATE INDEX idx_match_date ON Match(MDate);
CREATE INDEX idx_match_teams ON Match(Home_Team_ID, Away_Team_ID);
CREATE INDEX idx_match_referee ON Match(Referee_ID);
CREATE INDEX idx_team_name ON Team(Name);
```

**Benefits**:
- Faster JOIN operations
- Optimized WHERE clause filtering
- Improved ORDER BY performance
- Accelerated GROUP BY aggregations

---

## Features & Capabilities

### Data Management
- Complete CRUD operations for all entities
- Batch data insertion with transaction support
- Data validation at database level
- Automatic timestamp tracking
- Composite attribute handling (Player names)

### Relationship Management
- Enforced one-to-many relationships (Team → Player, Team → Medical Staff)
- Managed many-to-many relationships (Team ↔ Match)
- Strict one-to-one assignments (Match → Referee)
- Flexible sponsorship partnerships

### Business Logic Implementation
- Contract period tracking (ContractStart/End)
- Match status workflow (Scheduled → Completed)
- Home/Away team designation
- Score tracking and validation
- Assignment date management

### Reporting Capabilities
- Team rosters with complete player details
- Match schedules with venue and official information
- Sponsorship revenue analysis
- Medical staff assignments
- Referee workload distribution
- League standings and statistics
- Contract expiration alerts

---

## Data Analytics & Reporting

### Sample Queries and Insights

#### 1. League Standings
```sql
SELECT 
    t.Name as Team_Name,
    COUNT(DISTINCT m.MID) as Matches_Played,
    SUM(CASE 
        WHEN (m.Home_Team_ID = t.Team_ID AND m.Home_Score > m.Away_Score) OR
             (m.Away_Team_ID = t.Team_ID AND m.Away_Score > m.Home_Score)
        THEN 1 ELSE 0 
    END) as Wins,
    SUM(CASE 
        WHEN m.Home_Score = m.Away_Score AND m.Status = 'Completed'
        THEN 1 ELSE 0 
    END) as Draws
FROM Team t
LEFT JOIN Match m ON (t.Team_ID = m.Home_Team_ID OR t.Team_ID = m.Away_Team_ID)
    AND m.Status = 'Completed'
GROUP BY t.Team_ID
ORDER BY Wins DESC, Goals_Scored DESC;
```

**Insights**: Win-loss records, goal differentials, league rankings

#### 2. Team Roster Report
```sql
SELECT 
    t.Name as Team_Name,
    p.Name as Player_Name,
    p.Position,
    p.Contract_Start,
    p.Contract_End,
    CAST((julianday(p.Contract_End) - julianday('now')) AS INTEGER) as Days_Until_Expiry
FROM Team t
JOIN Player p ON t.Team_ID = p.Team_ID
ORDER BY t.Name, p.Position;
```

**Insights**: Complete squad composition, contract management, HR planning

#### 3. Sponsorship Revenue Analysis
```sql
SELECT 
    t.Name as Team_Name,
    COUNT(hs.SID) as Sponsor_Count,
    SUM(hs.Sponsorship_Amount) as Total_Revenue
FROM Team t
LEFT JOIN Has_Sponsor hs ON t.Team_ID = hs.Team_ID
GROUP BY t.Team_ID
ORDER BY Total_Revenue DESC;
```

**Insights**: Financial health, partnership diversity, revenue distribution

#### 4. Match Participation Analysis
```sql
SELECT 
    m.MDate,
    ht.Name as Home_Team,
    at.Name as Away_Team,
    m.Home_Score,
    m.Away_Score,
    r.Name as Referee,
    m.Location
FROM Match m
JOIN Team ht ON m.Home_Team_ID = ht.Team_ID
JOIN Team at ON m.Away_Team_ID = at.Team_ID
LEFT JOIN Referee r ON m.Referee_ID = r.RID
WHERE m.Status = 'Completed'
ORDER BY m.MDate DESC;
```

**Insights**: Historical match results, venue utilization, referee assignments

#### 5. Medical Staff Distribution
```sql
SELECT 
    t.Name as Team_Name,
    ms.Name as Medical_Staff,
    ms.Role,
    hms.Role_Description
FROM Team t
JOIN Has_Medical_Staff hms ON t.Team_ID = hms.Team_ID
JOIN Medical_Staff ms ON hms.MedID = ms.MedID
ORDER BY t.Name, ms.Role;
```

**Insights**: Healthcare resource allocation, team support structure

#### 6. Player Position Distribution
```sql
SELECT 
    Position,
    COUNT(*) as Player_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Player), 2) as Percentage
FROM Player
GROUP BY Position
ORDER BY Player_Count DESC;
```

**Insights**: Squad composition balance, positional depth

#### 7. Referee Workload Analysis
```sql
SELECT 
    r.Name as Referee_Name,
    COUNT(DISTINCT m.MID) as Matches_Officiated,
    GROUP_CONCAT(DISTINCT hr.Referee_Role) as Roles
FROM Referee r
LEFT JOIN Match m ON r.RID = m.Referee_ID
LEFT JOIN Have_Referee hr ON r.RID = hr.RID
GROUP BY r.RID
ORDER BY Matches_Officiated DESC;
```

**Insights**: Fair distribution of assignments, workload management

---

## System Advantages

### Data Integrity
- **Enforced Relationships**: Foreign keys prevent invalid references
- **Constraint Validation**: CHECK constraints ensure logical data
- **Unique Identifiers**: Primary keys guarantee record uniqueness
- **Referential Actions**: Cascading maintains consistency
- **Normalized Structure**: Reduces redundancy and anomalies

### Performance
- **Indexed Queries**: Strategic indexes accelerate lookups
- **Optimized Joins**: Efficient relationship traversal
- **Batch Operations**: Transaction support for bulk changes
- **Query Optimization**: SQLite query planner

### Scalability
- **Modular Design**: Easy to add new entities
- **Extensible Relationships**: Junction tables support growth
- **Normalized Schema**: Adding data doesn't require restructuring
- **Flexible Constraints**: Can adapt to rule changes

### Maintainability
- **Clear Structure**: Well-documented schema
- **Separation of Concerns**: Entities represent distinct concepts
- **Minimal Redundancy**: Changes update in one location
- **Version Control**: SQL scripts track schema evolution

### Business Value
- **Faster Reporting**: Queries replace manual compilation
- **Data Accuracy**: Constraints prevent errors before entry
- **Decision Support**: Analytics enable informed choices
- **Operational Efficiency**: Automated relationship management
- **Audit Trail**: Timestamps track data lifecycle

---

## Technical Specifications

### Database Details
- **Database File**: `sports_league.db`
- **Size**: Approximately 60KB (with sample data)
- **Tables**: 10 (6 entity tables, 4 junction tables)
- **Indexes**: 6 strategic indexes
- **Constraints**: 15+ foreign keys, 5+ check constraints

### Sample Data Volume
- 8 Teams
- 15 Players
- 8 Matches (5 completed, 3 scheduled)
- 6 Referees
- 6 Medical Staff Members
- 6 Sponsors
- 7 Medical Staff Assignments
- 8 Sponsorship Agreements
- 10 Team-Match Relationships
- 7 Referee-Match Assignments

### Technology Stack
- **Database**: SQLite 3.x
- **Programming Language**: Python 3.7+
- **Libraries**: 
  - `sqlite3`: Database connectivity
  - `pandas`: Data analysis and manipulation
  - `datetime`: Date/time handling

---

## Getting Started

### Prerequisites
```bash
# Python 3.7 or higher
python --version

# Required libraries
pip install pandas
```


## Usage Examples

### Adding a New Team
```python
cursor.execute('''
    INSERT INTO Team (Name, City, CoachID)
    VALUES (?, ?, ?)
''', ('Phoenix Suns', 'Phoenix', 2001))
conn.commit()
```

### Registering a Player
```python
cursor.execute('''
    INSERT INTO Player (Name, Position, Team_ID, Contract_Start, Contract_End)
    VALUES (?, ?, ?, ?, ?)
''', ('Michael Jordan', 'Forward', 1, '2024-01-01', '2026-12-31'))
conn.commit()
```

### Scheduling a Match
```python
cursor.execute('''
    INSERT INTO Match (MDate, Location, Home_Team_ID, Away_Team_ID, Referee_ID)
    VALUES (?, ?, ?, ?, ?)
''', ('2026-03-15', 'Madison Square Garden', 1, 2, 1))
conn.commit()
```

### Recording Match Result
```python
cursor.execute('''
    UPDATE Match 
    SET Home_Score = ?, Away_Score = ?, Status = 'Completed'
    WHERE MID = ?
''', (3, 2, 1))
conn.commit()
```

### Assigning Medical Staff
```python
cursor.execute('''
    INSERT INTO Has_Medical_Staff (MedID, Team_ID, Assignment_Date, Role_Description)
    VALUES (?, ?, ?, ?)
''', (1, 1, '2024-01-01', 'Primary team physician'))
conn.commit()
```

### Adding Sponsorship Deal
```python
cursor.execute('''
    INSERT INTO Has_Sponsor (SID, Team_ID, Sponsorship_Amount, Start_Date, End_Date)
    VALUES (?, ?, ?, ?, ?)
''', (1, 1, 500000.00, '2024-01-01', '2026-12-31'))
conn.commit()
```

### Exporting Data to CSV
```python
import pandas as pd

# Export team data
query = "SELECT * FROM Team"
df = pd.read_sql_query(query, conn)
df.to_csv('teams_export.csv', index=False)

# Export player data
query = "SELECT * FROM Player"
df = pd.read_sql_query(query, conn)
df.to_csv('players_export.csv', index=False)
```

---

## Future Enhancements

### Performance Optimization
- **Advanced Indexing**: Composite indexes for complex queries
- **Query Optimization**: Materialized views for frequent reports
- **Partitioning**: Table partitioning for large datasets
- **Caching**: Result caching for dashboard queries

### Automation
- **Stored Procedures**: Encapsulate common operations
- **Triggers**: Automatic data validation and logging
- **Scheduled Jobs**: Automated report generation
- **Event Listeners**: Real-time data synchronization

### Security
- **Role-Based Access Control (RBAC)**: User permission management
- **Data Encryption**: At-rest and in-transit encryption
- **Audit Logging**: Track all data modifications
- **SQL Injection Prevention**: Parameterized queries (already implemented)

### Feature Expansion
- **Historical Tracking**: Player transfer history, team evolution
- **Statistical Analysis**: Advanced metrics and analytics
- **Multi-League Support**: Manage multiple leagues in one database
- **Venue Management**: Stadium/facility tracking
- **Ticket Sales**: Integration with ticketing system
- **Injury Tracking**: Detailed medical history
- **Training Records**: Practice and fitness data
- **Social Media**: Integration with fan engagement platforms

### Integration
- **API Development**: REST API for external access
- **Web Interface**: Admin dashboard for non-technical users
- **Mobile App**: Real-time updates and notifications
- **BI Tools**: Integration with Tableau, Power BI
- **Third-Party Services**: Payment processing, streaming platforms

### Data Quality
- **Data Validation**: Enhanced constraint checking
- **Duplicate Detection**: Fuzzy matching algorithms
- **Data Cleansing**: Automated cleanup routines
- **Import Tools**: Bulk data migration utilities

---

## Key Takeaways

### Database Design Principles
1. **Strong relational design is critical for data accuracy and scalability**
   - Proper entity identification prevents data anomalies
   - Relationship modeling ensures logical data flow

2. **Normalization improves maintainability**
   - 3NF reduces redundancy
   - Single source of truth for each data point
   - Changes propagate correctly through relationships

3. **Constraints prevent errors before they occur**
   - Foreign keys enforce valid references
   - CHECK constraints validate business rules
   - UNIQUE constraints prevent duplicates

4. **SQL querying enables powerful analytics beyond simple storage**
   - Complex JOINs reveal insights
   - Aggregate functions provide summaries
   - Subqueries enable sophisticated filtering

5. **Database architecture directly supports business operations**
   - Faster reporting → better decisions
   - Data integrity → operational efficiency
   - Scalability → growth support

### Professional Skills Demonstrated
- Relational database modeling (ERD creation)
- SQL DDL (Data Definition Language)
- SQL DML (Data Manipulation Language)
- SQL DQL (Data Query Language)
- Normalization theory and application
- Constraint design and implementation
- Index strategy and optimization
- Python-Database integration
- Data analysis with Pandas
- Technical documentation

### Real-World Applications
- Sports league management systems
- Enterprise resource planning (ERP)
- Customer relationship management (CRM)
- Inventory management systems
- Human resources information systems (HRIS)
- Financial tracking applications
- Healthcare management platforms

---

## License

This project is provided as-is for educational and demonstration purposes. Feel free to use, modify, and distribute with appropriate attribution.

---

## Author - Abirami Baskaran

**Project Type**: Academi  Project  
**Focus**: Database Design, SQL Development, Data Analytics  
**Technologies**: SQLite, Python, SQL, Pandas  

---

## Acknowledgments

- SQLite Development Team for robust database engine
- Python Software Foundation for excellent programming language
- Pandas Development Team for powerful data analysis tools
- Database design principles from academic research and industry best practices
- Academic Project

---

## Contact & Support

For questions, suggestions, or issues:
Linkdln - https://www.linkedin.com/in/abiramihi/

---

## Conclusion

AthletaBase demonstrates how proper database architecture transforms raw data into a strategic business asset. By implementing industry-standard design principles—normalization, constraint enforcement, and relationship modeling—the system ensures data accuracy, enables powerful analytics, and supports scalable growth.

This project showcases the practical application of database theory to solve real-world business problems. The combination of strong technical implementation and clear documentation makes it both a functional system and an educational resource.

**The core message**: Well-designed databases are the foundation of data-driven decision-making. When data integrity is guaranteed at the architectural level, organizations can focus on extracting insights rather than correcting errors.

---

**Last Updated**: February 2026  
**Version**: 1.0  
**Database Version**: SQLite 3.x  
**Status**: Production-Ready Demo
