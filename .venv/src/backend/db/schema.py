import sqlite3

def create_job_ads_table():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_ads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_raw TEXT NOT NULL,
        company TEXT NOT NULL,
        schedule TEXT CHECK(status IN ('Full time', 'Part time')),
        location TEXT NOT NULL,
        salary TEXT,
        experience_min REAL,
        education TEXT,
        url TEXT,
        description TEXT NOT NULL,
        date_posted DATE NOT NULL,
        source TEXT NOT NULL,
        status TEXT CHECK(status IN ('Success', 'Declined', 'Irrelevant', 'Waiting')),
        progress TEXT,
        CONSTRAINT ad UNIQUE (url, description)
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
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
        job_ad_id INTEGER,
        skill_id INTEGER,
        type TEXT CHECK(type IN ('required', 'bonus')) DEFAULT 'required',
        FOREIGN KEY (job_ad_id) REFERENCES job_ads(id),
        FOREIGN KEY (skill_id) REFERENCES skills(id),
        CONSTRAINT unique_link UNIQUE (job_ad_id, skill_id)
    )
    """)
    conn.commit()
    conn.close()
    print("link table job ad + skill is created.")

def create_formats_table():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS formats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        UNIQUE (name)
    )
    """)
    conn.commit()
    conn.close()
    print("formats table is created.")

def create_jobad_format_table():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS link_jobad_format (
        job_ad_id INTEGER,
        format_id INTEGER,
        FOREIGN KEY (job_ad_id) REFERENCES job_ads(id),
        FOREIGN KEY (format_id) REFERENCES formats(id),
        CONSTRAINT unique_link UNIQUE (job_ad_id, format_id)
    )
    """)
    conn.commit()
    conn.close()
    print("link table job ad + format is created.")