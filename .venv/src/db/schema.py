import sqlite3

def create_job_ads_table():
    conn = sqlite3.connect("jobs.db")
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

def create_skills_table():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        ID integer PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        UNIQUE (name)
    )
    """)
    conn.commit()
    conn.close()
    print("skills table is created.")

def create_jobad_skill_table():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS link_jobad_skill (
        JobAdID integer,
        SkillID integer,
        Type text CHECK(type IN ('required', 'bonus')) DEFAULT 'required',
        FOREIGN KEY (JobAdID) REFERENCES job_ads(ID),
        FOREIGN KEY (SkillID) REFERENCES skills(ID),
        CONSTRAINT unique_link UNIQUE (JobAdID, SkillID)
    )
    """)
    conn.commit()
    conn.close()
    print("link table job ad + skill is created.")

def create_jobs_norm_table():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs_normal (
        ID integer PRIMARY KEY AUTOINCREMENT,
        Name text NOT NULL,
        UNIQUE (name)
    )
    """)
    conn.commit()
    conn.close()
    print("normalized jobs table is created.")