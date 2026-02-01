{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKRdNm4oTCr6731h4ZdRS1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Abirami-Baskaran-s/AthletaBase---Sports-Data-Architecture/blob/main/AthletaBase_Sports_Data_Architecture_SQL.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BHRZSnipo-Ka",
        "outputId": "a04ec4ce-3e93-4fe1-819a-891959a0d7a0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Libraries imported successfully!\n"
          ]
        }
      ],
      "source": [
        "import sqlite3\n",
        "from datetime import datetime, date\n",
        "import pandas as pd\n",
        "\n",
        "print(\"Libraries imported successfully!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "conn = sqlite3.connect('sports_league.db')\n",
        "cursor = conn.cursor()\n",
        "\n",
        "print(\"Database connection established\")\n",
        "print(\"Database: sports_league.db\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vNVHMNVUssQb",
        "outputId": "0028bb9c-83ff-491a-bc65-74eda7c4d181"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Database connection established\n",
            "Database: sports_league.db\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Medical_Staff (\n",
        "    MedID INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    Name VARCHAR(100) NOT NULL,\n",
        "    Role VARCHAR(50) NOT NULL,\n",
        "    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Medical_Staff table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0vh-bCDGsuya",
        "outputId": "833684dc-a28c-473b-aef0-ad23440c0457"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Medical_Staff table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Sponsor (\n",
        "    SID INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    Name VARCHAR(100) NOT NULL,\n",
        "    Type VARCHAR(50),\n",
        "    Contact_Details TEXT,\n",
        "    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Sponsor table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rOzpTAVAs1ih",
        "outputId": "a9a89bbe-248b-4705-a08f-b2590256734e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sponsor table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Referee (\n",
        "    RID INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    Name VARCHAR(100) NOT NULL,\n",
        "    Phone_No VARCHAR(20),\n",
        "    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Referee table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oXI6OZwbs5pg",
        "outputId": "d5ef3860-374b-432a-efd0-4bca9173de1c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Referee table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Team (\n",
        "    Team_ID INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    Name VARCHAR(100) NOT NULL UNIQUE,\n",
        "    City VARCHAR(100),\n",
        "    CoachID INTEGER,\n",
        "    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Team table created\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rp3jv-HCs9rh",
        "outputId": "d969967b-5c31-45dc-b147-0f3c4973f644"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Team table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Player (\n",
        "    PID INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    Name VARCHAR(100) NOT NULL,\n",
        "    Phone_No VARCHAR(20),\n",
        "    DOB DATE,\n",
        "    Address TEXT,\n",
        "    Position VARCHAR(50),\n",
        "    Contract_Start DATE,\n",
        "    Contract_End DATE,\n",
        "    Team_ID INTEGER,\n",
        "    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n",
        "    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID) ON DELETE SET NULL\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Player table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DMp0cQMetCZa",
        "outputId": "4b97f63b-9f82-44b4-c37c-edeb8a838f3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Player table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Match (\n",
        "    MID INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "    MDate DATE NOT NULL,\n",
        "    Location VARCHAR(200),\n",
        "    Referee_ID INTEGER,\n",
        "    Home_Team_ID INTEGER,\n",
        "    Away_Team_ID INTEGER,\n",
        "    Home_Score INTEGER DEFAULT 0,\n",
        "    Away_Score INTEGER DEFAULT 0,\n",
        "    Status VARCHAR(20) DEFAULT 'Scheduled',\n",
        "    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n",
        "    FOREIGN KEY (Referee_ID) REFERENCES Referee(RID),\n",
        "    FOREIGN KEY (Home_Team_ID) REFERENCES Team(Team_ID),\n",
        "    FOREIGN KEY (Away_Team_ID) REFERENCES Team(Team_ID),\n",
        "    CHECK (Home_Team_ID != Away_Team_ID)\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Match table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eD8q-kEttHsc",
        "outputId": "51e1138e-a421-43bc-b1ad-f65233d9e3cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Match table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Has_Medical_Staff (\n",
        "    MedID INTEGER,\n",
        "    Team_ID INTEGER,\n",
        "    Assignment_Date DATE DEFAULT (date('now')),\n",
        "    Role_Description TEXT,\n",
        "    PRIMARY KEY (MedID, Team_ID),\n",
        "    FOREIGN KEY (MedID) REFERENCES Medical_Staff(MedID) ON DELETE CASCADE,\n",
        "    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID) ON DELETE CASCADE\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Has_Medical_Staff junction table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jbrhG1JStPsJ",
        "outputId": "d1394ccf-9603-42b6-f071-4e1f16fcf468"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Has_Medical_Staff junction table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Has_Sponsor (\n",
        "    SID INTEGER,\n",
        "    Team_ID INTEGER,\n",
        "    Sponsorship_Amount DECIMAL(15, 2),\n",
        "    Start_Date DATE,\n",
        "    End_Date DATE,\n",
        "    Contract_Details TEXT,\n",
        "    PRIMARY KEY (SID, Team_ID),\n",
        "    FOREIGN KEY (SID) REFERENCES Sponsor(SID) ON DELETE CASCADE,\n",
        "    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID) ON DELETE CASCADE\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Has_Sponsor junction table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y-wPtyQ9tVNy",
        "outputId": "2cecbddb-f4a9-44a5-e69a-7dff3595efd2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Has_Sponsor junction table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Play (\n",
        "    Team_ID INTEGER,\n",
        "    MID INTEGER,\n",
        "    Team_Type VARCHAR(10) CHECK(Team_Type IN ('HOME', 'AWAY')),\n",
        "    Team_Score INTEGER DEFAULT 0,\n",
        "    PRIMARY KEY (Team_ID, MID),\n",
        "    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID) ON DELETE CASCADE,\n",
        "    FOREIGN KEY (MID) REFERENCES Match(MID) ON DELETE CASCADE\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Play junction table created\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aQy1ERzttZkY",
        "outputId": "b44a7d28-3a98-4b4b-d638-f80625c1ebe6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Play junction table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor.execute('''\n",
        "CREATE TABLE IF NOT EXISTS Have_Referee (\n",
        "    RID INTEGER,\n",
        "    MID INTEGER,\n",
        "    Referee_Role VARCHAR(50) DEFAULT 'Main Referee',\n",
        "    PRIMARY KEY (RID, MID),\n",
        "    FOREIGN KEY (RID) REFERENCES Referee(RID) ON DELETE CASCADE,\n",
        "    FOREIGN KEY (MID) REFERENCES Match(MID) ON DELETE CASCADE\n",
        ")\n",
        "''')\n",
        "conn.commit()\n",
        "print(\"Have_Referee junction table created\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RaiuKjIYtgA-",
        "outputId": "fc97590a-cf29-4c2d-89ac-f56a219fdac0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Have_Referee junction table created\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "indexes = [\n",
        "    \"CREATE INDEX IF NOT EXISTS idx_player_team ON Player(Team_ID)\",\n",
        "    \"CREATE INDEX IF NOT EXISTS idx_player_position ON Player(Position)\",\n",
        "    \"CREATE INDEX IF NOT EXISTS idx_match_date ON Match(MDate)\",\n",
        "    \"CREATE INDEX IF NOT EXISTS idx_match_teams ON Match(Home_Team_ID, Away_Team_ID)\",\n",
        "    \"CREATE INDEX IF NOT EXISTS idx_match_referee ON Match(Referee_ID)\",\n",
        "    \"CREATE INDEX IF NOT EXISTS idx_team_name ON Team(Name)\"\n",
        "]\n",
        "\n",
        "for index in indexes:\n",
        "    cursor.execute(index)\n",
        "\n",
        "conn.commit()\n",
        "print(\"All indexes created successfully\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sZvfSuj_tlgp",
        "outputId": "c42b4aac-2b98-4be5-f7ff-dca30352b23b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "All indexes created successfully\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "medical_staff_data = [\n",
        "    ('Dr. Sarah Johnson', 'Team Physician'),\n",
        "    ('Mike Thompson', 'Physiotherapist'),\n",
        "    ('Emily Chen', 'Sports Therapist'),\n",
        "    ('Dr. James Wilson', 'Orthopedic Specialist'),\n",
        "    ('Laura Martinez', 'Nutritionist'),\n",
        "    ('David Kim', 'Massage Therapist')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Medical_Staff (Name, Role)\n",
        "    VALUES (?, ?)\n",
        "''', medical_staff_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Medical Staff records inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_9gUrvKatrky",
        "outputId": "7bd5e0d2-9328-4735-b8c1-4cdb7b79097b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 6 Medical Staff records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sponsor_data = [\n",
        "    ('SportsCo Inc', 'Main Sponsor', 'contact@sportsco.com | +1-800-SPORTS'),\n",
        "    ('Energy Drink Plus', 'Beverage Partner', 'info@energydrink.com'),\n",
        "    ('Athletic Gear', 'Equipment Sponsor', 'sales@athleticgear.com'),\n",
        "    ('Tech Solutions', 'Technology Partner', 'support@techsolutions.com'),\n",
        "    ('Fitness World', 'Training Partner', 'hello@fitnessworld.com'),\n",
        "    ('Media Corp', 'Broadcasting Partner', 'contact@mediacorp.com')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Sponsor (Name, Type, Contact_Details)\n",
        "    VALUES (?, ?, ?)\n",
        "''', sponsor_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Sponsor records inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FAH3D71ktyTy",
        "outputId": "a45a7304-78b1-434a-9f63-4c16622b58fc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 6 Sponsor records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "referee_data = [\n",
        "    ('John Martinez', '+1-555-0101'),\n",
        "    ('Lisa Anderson', '+1-555-0102'),\n",
        "    ('Robert Taylor', '+1-555-0103'),\n",
        "    ('Maria Garcia', '+1-555-0104'),\n",
        "    ('David Brown', '+1-555-0105'),\n",
        "    ('Jennifer Wilson', '+1-555-0106')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Referee (Name, Phone_No)\n",
        "    VALUES (?, ?)\n",
        "''', referee_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Referee records inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "apetgzTVt2da",
        "outputId": "3b6d6092-d9f2-45de-f619-e75a1dc1312b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 6 Referee records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "team_data = [\n",
        "    ('Thunder Hawks', 'New York', 1001),\n",
        "    ('Lightning Strikes', 'Los Angeles', 1002),\n",
        "    ('Storm Chasers', 'Chicago', 1003),\n",
        "    ('Fire Dragons', 'Houston', 1004),\n",
        "    ('Ice Wolves', 'Boston', 1005),\n",
        "    ('Wave Riders', 'Miami', 1006),\n",
        "    ('Mountain Lions', 'Denver', 1007),\n",
        "    ('Desert Eagles', 'Phoenix', 1008)\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Team (Name, City, CoachID)\n",
        "    VALUES (?, ?, ?)\n",
        "''', team_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Team records inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dzjQs6Not6Ra",
        "outputId": "ff37e2c0-da0e-43fa-8ce1-b6b96e661746"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 8 Team records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "player_data = [\n",
        "    ('Alex Morgan', '+1-555-1001', '1995-03-15', '123 Main St, New York', 'Forward', '2024-01-01', '2026-12-31', 1),\n",
        "    ('Chris Evans', '+1-555-1002', '1993-07-22', '456 Oak Ave, New York', 'Midfielder', '2023-06-01', '2025-05-31', 1),\n",
        "    ('Sam Wilson', '+1-555-1003', '1996-11-30', '789 Pine Rd, New York', 'Defender', '2024-02-15', '2026-02-14', 1),\n",
        "    ('Jordan Lee', '+1-555-1004', '1996-11-30', '789 Pine Rd, Los Angeles', 'Defender', '2024-02-15', '2026-02-14', 2),\n",
        "    ('Taylor Swift', '+1-555-1005', '1994-05-18', '321 Elm St, Los Angeles', 'Goalkeeper', '2023-08-01', '2025-07-31', 2),\n",
        "    ('Blake Anderson', '+1-555-1006', '1997-09-09', '654 Maple Dr, Los Angeles', 'Forward', '2024-03-01', '2027-02-28', 2),\n",
        "    ('Morgan Freeman', '+1-555-1007', '1997-09-09', '654 Maple Dr, Chicago', 'Forward', '2024-03-01', '2027-02-28', 3),\n",
        "    ('Casey Johnson', '+1-555-1008', '1995-12-25', '987 Cedar Ln, Chicago', 'Midfielder', '2023-09-15', '2025-09-14', 3),\n",
        "    ('Riley Davis', '+1-555-1009', '1994-08-10', '246 Birch Ave, Chicago', 'Defender', '2024-01-15', '2026-01-14', 3),\n",
        "    ('Jamie Parker', '+1-555-1010', '1998-02-28', '135 Spruce St, Houston', 'Goalkeeper', '2024-04-01', '2026-03-31', 4),\n",
        "    ('Drew Mitchell', '+1-555-1011', '1995-06-14', '864 Walnut Rd, Houston', 'Midfielder', '2023-11-01', '2025-10-31', 4),\n",
        "    ('Quinn Roberts', '+1-555-1012', '1996-10-05', '975 Ash Ln, Boston', 'Forward', '2024-05-15', '2027-05-14', 5),\n",
        "    ('Avery Thompson', '+1-555-1013', '1997-04-20', '753 Poplar Dr, Boston', 'Defender', '2023-12-01', '2025-11-30', 5),\n",
        "    ('Cameron White', '+1-555-1014', '1994-11-12', '159 Willow Way, Miami', 'Goalkeeper', '2024-02-01', '2026-01-31', 6),\n",
        "    ('Jordan Hayes', '+1-555-1015', '1996-07-08', '357 Dogwood St, Miami', 'Midfielder', '2024-06-01', '2027-05-31', 6)\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Player (Name, Phone_No, DOB, Address, Position, Contract_Start, Contract_End, Team_ID)\n",
        "    VALUES (?, ?, ?, ?, ?, ?, ?, ?)\n",
        "''', player_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Player records inserted\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1y6KI1PWt-Z_",
        "outputId": "78fa366e-d05c-4bd0-9aa7-7a3afb4ae80e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 15 Player records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "match_data = [\n",
        "    ('2026-01-15', 'Yankee Stadium, NY', 1, 1, 2, 3, 2, 'Completed'),\n",
        "    ('2026-01-22', 'Staples Center, LA', 2, 2, 3, 1, 1, 'Completed'),\n",
        "    ('2026-01-29', 'United Center, Chicago', 3, 3, 4, 2, 4, 'Completed'),\n",
        "    ('2026-02-05', 'Toyota Center, Houston', 4, 4, 5, 3, 1, 'Completed'),\n",
        "    ('2026-02-12', 'TD Garden, Boston', 1, 5, 6, 2, 2, 'Completed'),\n",
        "    ('2026-02-19', 'American Airlines Arena, Miami', 2, 6, 1, 1, 3, 'Scheduled'),\n",
        "    ('2026-02-26', 'Ball Arena, Denver', 3, 7, 2, 0, 0, 'Scheduled'),\n",
        "    ('2026-03-05', 'Footprint Center, Phoenix', 4, 8, 3, 0, 0, 'Scheduled')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Match (MDate, Location, Referee_ID, Home_Team_ID, Away_Team_ID, Home_Score, Away_Score, Status)\n",
        "    VALUES (?, ?, ?, ?, ?, ?, ?, ?)\n",
        "''', match_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Match records inserted\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "40nmOai3uDCG",
        "outputId": "eae6526a-8228-4e8a-b27d-4274ea9cff87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 8 Match records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "medical_assignments = [\n",
        "    (1, 1, '2024-01-01', 'Primary team physician'),\n",
        "    (2, 1, '2024-01-01', 'Team physiotherapist'),\n",
        "    (3, 2, '2024-01-01', 'Sports therapy specialist'),\n",
        "    (4, 3, '2024-01-01', 'Orthopedic consultant'),\n",
        "    (5, 4, '2024-01-01', 'Nutrition advisor'),\n",
        "    (6, 5, '2024-01-01', 'Recovery specialist'),\n",
        "    (1, 6, '2024-02-01', 'Consulting physician')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Has_Medical_Staff (MedID, Team_ID, Assignment_Date, Role_Description)\n",
        "    VALUES (?, ?, ?, ?)\n",
        "''', medical_assignments)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Medical Staff assignments inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z1FDlYQsuHke",
        "outputId": "85197e42-d8a4-4692-db16-e2c28da26fec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 7 Medical Staff assignments inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sponsorship_data = [\n",
        "    (1, 1, 500000.00, '2024-01-01', '2026-12-31', 'Main jersey sponsor'),\n",
        "    (2, 1, 200000.00, '2024-01-01', '2025-12-31', 'Official beverage'),\n",
        "    (3, 2, 450000.00, '2024-01-01', '2026-12-31', 'Equipment provider'),\n",
        "    (4, 3, 300000.00, '2024-01-01', '2025-12-31', 'Technology partner'),\n",
        "    (5, 4, 350000.00, '2024-01-01', '2026-12-31', 'Training facility sponsor'),\n",
        "    (6, 5, 275000.00, '2024-01-01', '2025-12-31', 'Media rights partner'),\n",
        "    (1, 6, 400000.00, '2024-02-01', '2026-12-31', 'Jersey sponsor'),\n",
        "    (3, 7, 325000.00, '2024-01-01', '2026-12-31', 'Official outfitter')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Has_Sponsor (SID, Team_ID, Sponsorship_Amount, Start_Date, End_Date, Contract_Details)\n",
        "    VALUES (?, ?, ?, ?, ?, ?)\n",
        "''', sponsorship_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Sponsorship records inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GiG25LApuMkx",
        "outputId": "d23b2a51-4c04-46b2-97c0-9cd6f6c9c23e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 8 Sponsorship records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "play_data = [\n",
        "    (1, 1, 'HOME', 3),\n",
        "    (2, 1, 'AWAY', 2),\n",
        "    (2, 2, 'HOME', 1),\n",
        "    (3, 2, 'AWAY', 1),\n",
        "    (3, 3, 'HOME', 2),\n",
        "    (4, 3, 'AWAY', 4),\n",
        "    (4, 4, 'HOME', 3),\n",
        "    (5, 4, 'AWAY', 1),\n",
        "    (5, 5, 'HOME', 2),\n",
        "    (6, 5, 'AWAY', 2)\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Play (Team_ID, MID, Team_Type, Team_Score)\n",
        "    VALUES (?, ?, ?, ?)\n",
        "''', play_data)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Play relationship records inserted\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bIfEJ4D8uRl5",
        "outputId": "cf291405-e665-4ae9-c16f-d1a6f61b9336"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 10 Play relationship records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "referee_assignments = [\n",
        "    (1, 1, 'Main Referee'),\n",
        "    (2, 1, 'Assistant Referee'),\n",
        "    (2, 2, 'Main Referee'),\n",
        "    (3, 3, 'Main Referee'),\n",
        "    (4, 4, 'Main Referee'),\n",
        "    (1, 5, 'Main Referee'),\n",
        "    (5, 5, 'Assistant Referee')\n",
        "]\n",
        "\n",
        "cursor.executemany('''\n",
        "    INSERT OR IGNORE INTO Have_Referee (RID, MID, Referee_Role)\n",
        "    VALUES (?, ?, ?)\n",
        "''', referee_assignments)\n",
        "\n",
        "conn.commit()\n",
        "print(f\"✓ {cursor.rowcount} Referee assignment records inserted\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mcPrHWIiuVBD",
        "outputId": "07121b21-eceb-4ffe-8b3f-582065e539e7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ 7 Referee assignment records inserted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tables = ['Medical_Staff', 'Sponsor', 'Referee', 'Team', 'Player', 'Match',\n",
        "          'Has_Medical_Staff', 'Has_Sponsor', 'Play', 'Have_Referee']\n",
        "\n",
        "print(\"\\n\" + \"=\"*50)\n",
        "print(\"DATABASE RECORD COUNTS\")\n",
        "print(\"=\"*50)\n",
        "\n",
        "for table in tables:\n",
        "    cursor.execute(f'SELECT COUNT(*) FROM {table}')\n",
        "    count = cursor.fetchone()[0]\n",
        "    print(f\"{table:.<30} {count:>5} records\")\n",
        "\n",
        "print(\"=\"*50)"
      ],
      "metadata": {
        "id": "VpNh2fL7uaJX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e7a2940a-e15a-45a2-c49e-7754254324fb"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "==================================================\n",
            "DATABASE RECORD COUNTS\n",
            "==================================================\n",
            "Medical_Staff.................     6 records\n",
            "Sponsor.......................     6 records\n",
            "Referee.......................     6 records\n",
            "Team..........................     8 records\n",
            "Player........................    15 records\n",
            "Match.........................     8 records\n",
            "Has_Medical_Staff.............     7 records\n",
            "Has_Sponsor...................     8 records\n",
            "Play..........................    10 records\n",
            "Have_Referee..................     7 records\n",
            "==================================================\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    t.Team_ID,\n",
        "    t.Name as Team_Name,\n",
        "    t.City,\n",
        "    COUNT(p.PID) as Player_Count\n",
        "FROM Team t\n",
        "LEFT JOIN Player p ON t.Team_ID = p.Team_ID\n",
        "GROUP BY t.Team_ID, t.Name, t.City\n",
        "ORDER BY t.Name\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nTEAMS WITH PLAYER COUNTS\")\n",
        "print(\"=\"*60)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w-3WYoT9896f",
        "outputId": "919fcc63-9fd7-46f6-e257-a3846c82acf9"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "TEAMS WITH PLAYER COUNTS\n",
            "============================================================\n",
            " Team_ID         Team_Name        City  Player_Count\n",
            "       8     Desert Eagles     Phoenix             0\n",
            "       4      Fire Dragons     Houston             2\n",
            "       5        Ice Wolves      Boston             2\n",
            "       2 Lightning Strikes Los Angeles             3\n",
            "       7    Mountain Lions      Denver             0\n",
            "       3     Storm Chasers     Chicago             3\n",
            "       1     Thunder Hawks    New York             3\n",
            "       6       Wave Riders       Miami             2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    p.PID,\n",
        "    p.Name as Player_Name,\n",
        "    p.Position,\n",
        "    t.Name as Team_Name,\n",
        "    t.City,\n",
        "    p.Contract_Start,\n",
        "    p.Contract_End\n",
        "FROM Player p\n",
        "LEFT JOIN Team t ON p.Team_ID = t.Team_ID\n",
        "ORDER BY t.Name, p.Position, p.Name\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nPLAYERS BY TEAM\")\n",
        "print(\"=\"*80)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "etQ0jLwX9D44",
        "outputId": "3aabd157-fc7f-46e2-9487-f33aecf2ae1e"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "PLAYERS BY TEAM\n",
            "================================================================================\n",
            " PID    Player_Name   Position         Team_Name        City Contract_Start Contract_End\n",
            "  10   Jamie Parker Goalkeeper      Fire Dragons     Houston     2024-04-01   2026-03-31\n",
            "  11  Drew Mitchell Midfielder      Fire Dragons     Houston     2023-11-01   2025-10-31\n",
            "  13 Avery Thompson   Defender        Ice Wolves      Boston     2023-12-01   2025-11-30\n",
            "  12  Quinn Roberts    Forward        Ice Wolves      Boston     2024-05-15   2027-05-14\n",
            "   4     Jordan Lee   Defender Lightning Strikes Los Angeles     2024-02-15   2026-02-14\n",
            "   6 Blake Anderson    Forward Lightning Strikes Los Angeles     2024-03-01   2027-02-28\n",
            "   5   Taylor Swift Goalkeeper Lightning Strikes Los Angeles     2023-08-01   2025-07-31\n",
            "   9    Riley Davis   Defender     Storm Chasers     Chicago     2024-01-15   2026-01-14\n",
            "   7 Morgan Freeman    Forward     Storm Chasers     Chicago     2024-03-01   2027-02-28\n",
            "   8  Casey Johnson Midfielder     Storm Chasers     Chicago     2023-09-15   2025-09-14\n",
            "   3     Sam Wilson   Defender     Thunder Hawks    New York     2024-02-15   2026-02-14\n",
            "   1    Alex Morgan    Forward     Thunder Hawks    New York     2024-01-01   2026-12-31\n",
            "   2    Chris Evans Midfielder     Thunder Hawks    New York     2023-06-01   2025-05-31\n",
            "  14  Cameron White Goalkeeper       Wave Riders       Miami     2024-02-01   2026-01-31\n",
            "  15   Jordan Hayes Midfielder       Wave Riders       Miami     2024-06-01   2027-05-31\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    m.MID,\n",
        "    m.MDate as Match_Date,\n",
        "    ht.Name as Home_Team,\n",
        "    m.Home_Score,\n",
        "    at.Name as Away_Team,\n",
        "    m.Away_Score,\n",
        "    m.Location,\n",
        "    r.Name as Referee,\n",
        "    m.Status\n",
        "FROM Match m\n",
        "JOIN Team ht ON m.Home_Team_ID = ht.Team_ID\n",
        "JOIN Team at ON m.Away_Team_ID = at.Team_ID\n",
        "LEFT JOIN Referee r ON m.Referee_ID = r.RID\n",
        "ORDER BY m.MDate DESC\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\n MATCH SCHEDULE & RESULTS\")\n",
        "print(\"=\"*100)\n",
        "print(df.to_string(index=False))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DAe0d9zo9Jon",
        "outputId": "833c91fb-76f4-4709-9140-d6fa4bf9d79d"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            " MATCH SCHEDULE & RESULTS\n",
            "====================================================================================================\n",
            " MID Match_Date         Home_Team  Home_Score         Away_Team  Away_Score                       Location       Referee    Status\n",
            "   8 2026-03-05     Desert Eagles           0     Storm Chasers           0      Footprint Center, Phoenix  Maria Garcia Scheduled\n",
            "   7 2026-02-26    Mountain Lions           0 Lightning Strikes           0             Ball Arena, Denver Robert Taylor Scheduled\n",
            "   6 2026-02-19       Wave Riders           1     Thunder Hawks           3 American Airlines Arena, Miami Lisa Anderson Scheduled\n",
            "   5 2026-02-12        Ice Wolves           2       Wave Riders           2              TD Garden, Boston John Martinez Completed\n",
            "   4 2026-02-05      Fire Dragons           3        Ice Wolves           1         Toyota Center, Houston  Maria Garcia Completed\n",
            "   3 2026-01-29     Storm Chasers           2      Fire Dragons           4         United Center, Chicago Robert Taylor Completed\n",
            "   2 2026-01-22 Lightning Strikes           1     Storm Chasers           1             Staples Center, LA Lisa Anderson Completed\n",
            "   1 2026-01-15     Thunder Hawks           3 Lightning Strikes           2             Yankee Stadium, NY John Martinez Completed\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    t.Name as Team_Name,\n",
        "    s.Name as Sponsor,\n",
        "    s.Type as Sponsor_Type,\n",
        "    hs.Sponsorship_Amount,\n",
        "    hs.Start_Date,\n",
        "    hs.End_Date,\n",
        "    hs.Contract_Details\n",
        "FROM Has_Sponsor hs\n",
        "JOIN Team t ON hs.Team_ID = t.Team_ID\n",
        "JOIN Sponsor s ON hs.SID = s.SID\n",
        "ORDER BY t.Name, hs.Sponsorship_Amount DESC\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nTEAM SPONSORSHIPS\")\n",
        "print(\"=\"*100)\n",
        "print(df.to_string(index=False))\n",
        "\n",
        "\n",
        "query2 = '''\n",
        "SELECT\n",
        "    t.Name as Team_Name,\n",
        "    COUNT(hs.SID) as Sponsor_Count,\n",
        "    SUM(hs.Sponsorship_Amount) as Total_Sponsorship\n",
        "FROM Team t\n",
        "LEFT JOIN Has_Sponsor hs ON t.Team_ID = hs.Team_ID\n",
        "GROUP BY t.Team_ID, t.Name\n",
        "ORDER BY Total_Sponsorship DESC\n",
        "'''\n",
        "\n",
        "df2 = pd.read_sql_query(query2, conn)\n",
        "print(\"\\nTOTAL SPONSORSHIP BY TEAM\")\n",
        "print(\"=\"*60)\n",
        "print(df2.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IcWaKwW19Qdq",
        "outputId": "e413aef4-74b1-4d86-feb5-52b18587990d"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "TEAM SPONSORSHIPS\n",
            "====================================================================================================\n",
            "        Team_Name           Sponsor         Sponsor_Type  Sponsorship_Amount Start_Date   End_Date          Contract_Details\n",
            "     Fire Dragons     Fitness World     Training Partner              350000 2024-01-01 2026-12-31 Training facility sponsor\n",
            "       Ice Wolves        Media Corp Broadcasting Partner              275000 2024-01-01 2025-12-31      Media rights partner\n",
            "Lightning Strikes     Athletic Gear    Equipment Sponsor              450000 2024-01-01 2026-12-31        Equipment provider\n",
            "   Mountain Lions     Athletic Gear    Equipment Sponsor              325000 2024-01-01 2026-12-31        Official outfitter\n",
            "    Storm Chasers    Tech Solutions   Technology Partner              300000 2024-01-01 2025-12-31        Technology partner\n",
            "    Thunder Hawks      SportsCo Inc         Main Sponsor              500000 2024-01-01 2026-12-31       Main jersey sponsor\n",
            "    Thunder Hawks Energy Drink Plus     Beverage Partner              200000 2024-01-01 2025-12-31         Official beverage\n",
            "      Wave Riders      SportsCo Inc         Main Sponsor              400000 2024-02-01 2026-12-31            Jersey sponsor\n",
            "\n",
            "TOTAL SPONSORSHIP BY TEAM\n",
            "============================================================\n",
            "        Team_Name  Sponsor_Count  Total_Sponsorship\n",
            "    Thunder Hawks              2           700000.0\n",
            "Lightning Strikes              1           450000.0\n",
            "      Wave Riders              1           400000.0\n",
            "     Fire Dragons              1           350000.0\n",
            "   Mountain Lions              1           325000.0\n",
            "    Storm Chasers              1           300000.0\n",
            "       Ice Wolves              1           275000.0\n",
            "    Desert Eagles              0                NaN\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    ms.Name as Medical_Staff,\n",
        "    ms.Role,\n",
        "    t.Name as Team_Name,\n",
        "    hms.Assignment_Date,\n",
        "    hms.Role_Description\n",
        "FROM Has_Medical_Staff hms\n",
        "JOIN Medical_Staff ms ON hms.MedID = ms.MedID\n",
        "JOIN Team t ON hms.Team_ID = t.Team_ID\n",
        "ORDER BY t.Name, ms.Role\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\n⚕️ MEDICAL STAFF ASSIGNMENTS\")\n",
        "print(\"=\"*100)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "11EbPbes9bO1",
        "outputId": "4704a731-daad-4d0b-f2ce-215ed2c0cffb"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "⚕️ MEDICAL STAFF ASSIGNMENTS\n",
            "====================================================================================================\n",
            "    Medical_Staff                  Role         Team_Name Assignment_Date          Role_Description\n",
            "   Laura Martinez          Nutritionist      Fire Dragons      2024-01-01         Nutrition advisor\n",
            "        David Kim     Massage Therapist        Ice Wolves      2024-01-01       Recovery specialist\n",
            "       Emily Chen      Sports Therapist Lightning Strikes      2024-01-01 Sports therapy specialist\n",
            " Dr. James Wilson Orthopedic Specialist     Storm Chasers      2024-01-01     Orthopedic consultant\n",
            "    Mike Thompson       Physiotherapist     Thunder Hawks      2024-01-01      Team physiotherapist\n",
            "Dr. Sarah Johnson        Team Physician     Thunder Hawks      2024-01-01    Primary team physician\n",
            "Dr. Sarah Johnson        Team Physician       Wave Riders      2024-02-01      Consulting physician\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    t.Name as Team_Name,\n",
        "    COUNT(DISTINCT m.MID) as Matches_Played,\n",
        "    SUM(CASE\n",
        "        WHEN (m.Home_Team_ID = t.Team_ID AND m.Home_Score > m.Away_Score) OR\n",
        "             (m.Away_Team_ID = t.Team_ID AND m.Away_Score > m.Home_Score)\n",
        "        THEN 1 ELSE 0\n",
        "    END) as Wins,\n",
        "    SUM(CASE\n",
        "        WHEN (m.Home_Team_ID = t.Team_ID AND m.Home_Score < m.Away_Score) OR\n",
        "             (m.Away_Team_ID = t.Team_ID AND m.Away_Score < m.Home_Score)\n",
        "        THEN 1 ELSE 0\n",
        "    END) as Losses,\n",
        "    SUM(CASE\n",
        "        WHEN m.Home_Score = m.Away_Score AND m.Status = 'Completed'\n",
        "        THEN 1 ELSE 0\n",
        "    END) as Draws,\n",
        "    SUM(CASE\n",
        "        WHEN m.Home_Team_ID = t.Team_ID THEN m.Home_Score\n",
        "        WHEN m.Away_Team_ID = t.Team_ID THEN m.Away_Score\n",
        "        ELSE 0\n",
        "    END) as Goals_Scored,\n",
        "    SUM(CASE\n",
        "        WHEN m.Home_Team_ID = t.Team_ID THEN m.Away_Score\n",
        "        WHEN m.Away_Team_ID = t.Team_ID THEN m.Home_Score\n",
        "        ELSE 0\n",
        "    END) as Goals_Conceded\n",
        "FROM Team t\n",
        "LEFT JOIN Match m ON (t.Team_ID = m.Home_Team_ID OR t.Team_ID = m.Away_Team_ID)\n",
        "    AND m.Status = 'Completed'\n",
        "GROUP BY t.Team_ID, t.Name\n",
        "ORDER BY Wins DESC, Goals_Scored DESC\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nTEAM STATISTICS\")\n",
        "print(\"=\"*100)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FXEOcWE19gDQ",
        "outputId": "80781a35-7d40-4b97-fd59-f842198d3456"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "TEAM STATISTICS\n",
            "====================================================================================================\n",
            "        Team_Name  Matches_Played  Wins  Losses  Draws  Goals_Scored  Goals_Conceded\n",
            "     Fire Dragons               2     2       0      0             7               3\n",
            "    Thunder Hawks               1     1       0      0             3               2\n",
            "       Ice Wolves               2     0       1      1             3               5\n",
            "Lightning Strikes               2     0       1      1             3               4\n",
            "    Storm Chasers               2     0       1      1             3               5\n",
            "      Wave Riders               1     0       0      1             2               2\n",
            "    Desert Eagles               0     0       0      0             0               0\n",
            "   Mountain Lions               0     0       0      0             0               0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    Position,\n",
        "    COUNT(*) as Player_Count,\n",
        "    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Player), 2) as Percentage\n",
        "FROM Player\n",
        "GROUP BY Position\n",
        "ORDER BY Player_Count DESC\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nPLAYER POSITION DISTRIBUTION\")\n",
        "print(\"=\"*60)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a1ngnUtw9rFM",
        "outputId": "ef6da3d5-0c3e-442b-8a8e-0c59413ad9a9"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "PLAYER POSITION DISTRIBUTION\n",
            "============================================================\n",
            "  Position  Player_Count  Percentage\n",
            "  Defender             4       26.67\n",
            "   Forward             4       26.67\n",
            "Midfielder             4       26.67\n",
            "Goalkeeper             3       20.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    m.MDate as Match_Date,\n",
        "    ht.Name as Home_Team,\n",
        "    at.Name as Away_Team,\n",
        "    m.Location,\n",
        "    r.Name as Referee\n",
        "FROM Match m\n",
        "JOIN Team ht ON m.Home_Team_ID = ht.Team_ID\n",
        "JOIN Team at ON m.Away_Team_ID = at.Team_ID\n",
        "LEFT JOIN Referee r ON m.Referee_ID = r.RID\n",
        "WHERE m.Status = 'Scheduled'\n",
        "ORDER BY m.MDate\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nUPCOMING MATCHES\")\n",
        "print(\"=\"*80)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CatB7nj590Az",
        "outputId": "e8dfeea4-e856-4ef8-9daf-bd780f5ad399"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "UPCOMING MATCHES\n",
            "================================================================================\n",
            "Match_Date      Home_Team         Away_Team                       Location       Referee\n",
            "2026-02-19    Wave Riders     Thunder Hawks American Airlines Arena, Miami Lisa Anderson\n",
            "2026-02-26 Mountain Lions Lightning Strikes             Ball Arena, Denver Robert Taylor\n",
            "2026-03-05  Desert Eagles     Storm Chasers      Footprint Center, Phoenix  Maria Garcia\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    r.Name as Referee_Name,\n",
        "    r.Phone_No,\n",
        "    COUNT(DISTINCT m.MID) as Matches_Officiated,\n",
        "    GROUP_CONCAT(DISTINCT hr.Referee_Role) as Roles\n",
        "FROM Referee r\n",
        "LEFT JOIN Match m ON r.RID = m.Referee_ID\n",
        "LEFT JOIN Have_Referee hr ON r.RID = hr.RID\n",
        "GROUP BY r.RID, r.Name, r.Phone_No\n",
        "ORDER BY Matches_Officiated DESC\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nREFEREE STATISTICS\")\n",
        "print(\"=\"*80)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ufzOEelj94W7",
        "outputId": "e2c5793b-aff7-454a-c05f-c0dcec9e6cbf"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "REFEREE STATISTICS\n",
            "================================================================================\n",
            "   Referee_Name    Phone_No  Matches_Officiated                          Roles\n",
            "  John Martinez +1-555-0101                   2                   Main Referee\n",
            "  Lisa Anderson +1-555-0102                   2 Assistant Referee,Main Referee\n",
            "  Robert Taylor +1-555-0103                   2                   Main Referee\n",
            "   Maria Garcia +1-555-0104                   2                   Main Referee\n",
            "    David Brown +1-555-0105                   0              Assistant Referee\n",
            "Jennifer Wilson +1-555-0106                   0                           None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    p.Name as Player_Name,\n",
        "    t.Name as Team_Name,\n",
        "    p.Position,\n",
        "    p.Contract_End,\n",
        "    CAST((julianday(p.Contract_End) - julianday('now')) AS INTEGER) as Days_Until_Expiry\n",
        "FROM Player p\n",
        "LEFT JOIN Team t ON p.Team_ID = t.Team_ID\n",
        "WHERE p.Contract_End IS NOT NULL\n",
        "ORDER BY p.Contract_End\n",
        "LIMIT 10\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nCONTRACT EXPIRATION TRACKER\")\n",
        "print(\"=\"*80)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VE7wiPCQ9_CF",
        "outputId": "d692e5d9-00a4-4f7e-f52d-8a809fbe535a"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "CONTRACT EXPIRATION TRACKER\n",
            "================================================================================\n",
            "   Player_Name         Team_Name   Position Contract_End  Days_Until_Expiry\n",
            "   Chris Evans     Thunder Hawks Midfielder   2025-05-31               -246\n",
            "  Taylor Swift Lightning Strikes Goalkeeper   2025-07-31               -185\n",
            " Casey Johnson     Storm Chasers Midfielder   2025-09-14               -140\n",
            " Drew Mitchell      Fire Dragons Midfielder   2025-10-31                -93\n",
            "Avery Thompson        Ice Wolves   Defender   2025-11-30                -63\n",
            "   Riley Davis     Storm Chasers   Defender   2026-01-14                -18\n",
            " Cameron White       Wave Riders Goalkeeper   2026-01-31                 -1\n",
            "    Sam Wilson     Thunder Hawks   Defender   2026-02-14                 12\n",
            "    Jordan Lee Lightning Strikes   Defender   2026-02-14                 12\n",
            "  Jamie Parker      Fire Dragons Goalkeeper   2026-03-31                 57\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "team_name = 'Thunder Hawks'\n",
        "\n",
        "query = f'''\n",
        "SELECT\n",
        "    'Team Information' as Category,\n",
        "    'Name: ' || t.Name || ', City: ' || t.City as Details\n",
        "FROM Team t\n",
        "WHERE t.Name = '{team_name}'\n",
        "\n",
        "UNION ALL\n",
        "\n",
        "SELECT\n",
        "    'Players' as Category,\n",
        "    'Total: ' || COUNT(*) as Details\n",
        "FROM Player p\n",
        "JOIN Team t ON p.Team_ID = t.Team_ID\n",
        "WHERE t.Name = '{team_name}'\n",
        "\n",
        "UNION ALL\n",
        "\n",
        "SELECT\n",
        "    'Sponsorships' as Category,\n",
        "    'Total Amount: $' || COALESCE(SUM(hs.Sponsorship_Amount), 0) as Details\n",
        "FROM Team t\n",
        "LEFT JOIN Has_Sponsor hs ON t.Team_ID = hs.Team_ID\n",
        "WHERE t.Name = '{team_name}'\n",
        "\n",
        "UNION ALL\n",
        "\n",
        "SELECT\n",
        "    'Medical Staff' as Category,\n",
        "    'Total: ' || COUNT(*) as Details\n",
        "FROM Team t\n",
        "LEFT JOIN Has_Medical_Staff hms ON t.Team_ID = hms.Team_ID\n",
        "WHERE t.Name = '{team_name}'\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(f\"\\nTEAM PROFILE: {team_name}\")\n",
        "print(\"=\"*60)\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RVd-ZVx6-FQp",
        "outputId": "ce3a649c-e937-49f1-9a26-f1bc2f531a15"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "TEAM PROFILE: Thunder Hawks\n",
            "============================================================\n",
            "        Category                             Details\n",
            "Team Information Name: Thunder Hawks, City: New York\n",
            "         Players                            Total: 3\n",
            "    Sponsorships               Total Amount: $700000\n",
            "   Medical Staff                            Total: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = '''\n",
        "SELECT\n",
        "    name as Table_Name,\n",
        "    type as Object_Type\n",
        "FROM sqlite_master\n",
        "WHERE type IN ('table', 'index')\n",
        "ORDER BY type, name\n",
        "'''\n",
        "\n",
        "df = pd.read_sql_query(query, conn)\n",
        "print(\"\\nDATABASE SCHEMA\")\n",
        "print(\"=\"*60)\n",
        "print(df.to_string(index=False))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1K_2EweD-RqC",
        "outputId": "d24f9207-21c5-48bb-b926-69cf2a432700"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "DATABASE SCHEMA\n",
            "============================================================\n",
            "                          Table_Name Object_Type\n",
            "                      idx_match_date       index\n",
            "                   idx_match_referee       index\n",
            "                     idx_match_teams       index\n",
            "                 idx_player_position       index\n",
            "                     idx_player_team       index\n",
            "                       idx_team_name       index\n",
            "sqlite_autoindex_Has_Medical_Staff_1       index\n",
            "      sqlite_autoindex_Has_Sponsor_1       index\n",
            "     sqlite_autoindex_Have_Referee_1       index\n",
            "             sqlite_autoindex_Play_1       index\n",
            "             sqlite_autoindex_Team_1       index\n",
            "                   Has_Medical_Staff       table\n",
            "                         Has_Sponsor       table\n",
            "                        Have_Referee       table\n",
            "                               Match       table\n",
            "                       Medical_Staff       table\n",
            "                                Play       table\n",
            "                              Player       table\n",
            "                             Referee       table\n",
            "                             Sponsor       table\n",
            "                                Team       table\n",
            "                     sqlite_sequence       table\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# Create exports directory\n",
        "os.makedirs('exports', exist_ok=True)\n",
        "\n",
        "tables_to_export = ['Team', 'Player', 'Match', 'Sponsor', 'Medical_Staff', 'Referee']\n",
        "\n",
        "for table in tables_to_export:\n",
        "    query = f'SELECT * FROM {table}'\n",
        "    df = pd.read_sql_query(query, conn)\n",
        "    filename = f'exports/{table}.csv'\n",
        "    df.to_csv(filename, index=False)\n",
        "    print(f\"✓ Exported {table} to {filename}\")\n",
        "\n",
        "print(\"\\nAll exports completed!\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H2CwyRKA-aZC",
        "outputId": "790d0376-0fb4-43e7-a2fe-5c2291ab6755"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ Exported Team to exports/Team.csv\n",
            "✓ Exported Player to exports/Player.csv\n",
            "✓ Exported Match to exports/Match.csv\n",
            "✓ Exported Sponsor to exports/Sponsor.csv\n",
            "✓ Exported Medical_Staff to exports/Medical_Staff.csv\n",
            "✓ Exported Referee to exports/Referee.csv\n",
            "\n",
            "All exports completed!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "conn.close()\n",
        "print(\"✓ Database connection closed successfully\")\n",
        "print(\"\\n\" + \"=\"*60)\n",
        "print(\"DATABASE OPERATIONS COMPLETE!\")\n",
        "print(\"=\"*60)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z8-6dWwV-f5p",
        "outputId": "b9cd557b-b47d-4e40-cab3-ad017d132631"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✓ Database connection closed successfully\n",
            "\n",
            "============================================================\n",
            "DATABASE OPERATIONS COMPLETE!\n",
            "============================================================\n"
          ]
        }
      ]
    }
  ]
}
