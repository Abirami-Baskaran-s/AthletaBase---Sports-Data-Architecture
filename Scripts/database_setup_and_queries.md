
<img width="596" height="706" alt="Screenshot 2026-01-23 at 11 15 37 AM" src="https://github.com/user-attachments/assets/22e20f07-ba1f-4e25-9e02-aa9d4b893ee5" />

🧩 Core Entity Architecture

The system is built around the Team entity, which serves as the central hub connecting athletic talent, administrative staff, and competitive events. All major operational components of the sports league are logically linked through this core entity.

Teams

Teams are defined by a unique TeamID, along with attributes such as team name and geographic location. The inclusion of CoachName highlights the leadership structure and managerial responsibility associated with each team.

Players

The Players entity captures individual athlete information using a composite name structure (FirstName, MiddleName, LastName). It also records professional details such as playing Position and contractual timelines (ContractStart and ContractEnd), enabling effective roster and contract management.

Support and Oversight

The system manages human resources through two key entities:

Medical Staff, categorized by role, ensuring player health and recovery management.

Referees, responsible for officiating matches and maintaining competitive fairness.

Together, these entities ensure both operational continuity and regulatory oversight within the league.

🔗 Relationship Dynamics and Cardinality

The database model defines the operational rules of the organization through clearly enforced relationships and cardinality constraints.

Competitive Infrastructure

Team to Match (M:N)
This many-to-many relationship reflects a league structure where teams participate in multiple matches throughout a season.

Match Specifics
Each Match functions as a junction entity, explicitly identifying a HomeTeamID and an AwayTeamID, ensuring clear competitive roles for each fixture.

Referee Assignment (1:1)
The model enforces a strict one-to-one relationship between referees and matches. Each match is officiated by one referee, and each referee is assigned to only one match at a time, ensuring accountability and integrity.

Organizational Management

Team to Player (1:M)
A one-to-many relationship allows each team to maintain a roster of players, while ensuring that each player is associated with only one team at any given time.

Team to Medical Staff (1:M)
Teams can employ multiple medical staff members (such as doctors and physiotherapists), while each staff member is assigned to a single team for focused healthcare management.

Financial and Commercial Support

Team to Sponsor (1:M)
This relationship supports a multiple-sponsorship model where a team can have several sponsors. In the current design, each sponsor is associated with one primary team partnership.

🔐 Data Integrity and Flow

The Enhanced Entity Relationship (EER) model ensures high data integrity through the structured use of Primary Keys (PK) and Foreign Keys (FK).

Relational Mapping
Foreign keys such as TeamID in the Players entity and RefereeID in the Matches entity create a connected data structure that enables complex queries, such as identifying players involved in matches officiated by a specific referee.

Accountability and Management
The inclusion of ContractStart and ContractEnd dates transforms the system from a simple record-keeping database into a functional management tool that supports contract tracking and administrative planning.

Normalization
Separating Medical Staff and Sponsors into independent entities reduces data redundancy and improves scalability. This design allows the organization to expand staff or sponsorships without modifying the core Teams table.

