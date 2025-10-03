import sqlite3

def create_job_ads_table():
    conn = sqlite3.connect("job_ads.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_ads (
        ID integer PRIMARY KEY AUTOINCREMENT,
        RawTitle text NOT NULL,
        Company text NOT NULL,
        Location text NOT NULL,
        Salary text,
        ExperienceYears real,
        Education text,
        Link text,
        Description text NOT NULL,
        DatePosted date NOT NULL,
        Source text NOT NULL,
        Status text CHECK(status IN ('success', 'declined', 'irrelevant', 'waiting')),
        Progress text,
        CONSTRAINT job UNIQUE (Link, Description)
    )
    """)
    conn.commit()
    conn.close()
    print("job_ads table is created.")



