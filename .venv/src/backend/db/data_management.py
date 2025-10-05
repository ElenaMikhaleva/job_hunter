import sqlite3

def insert_job_ad(job_data, descr):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO job_ads (
            title_raw, company, schedule, location, experience_min, salary, description, url, date_posted, source
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        job_data["title_raw"],
        job_data["company"],
        job_data["schedule"],
        job_data["location"],
        job_data["experience"],
        job_data["salary"],
        descr,
        job_data["url"],
        job_data["date_posted"],
        job_data["source"]
    ))
    conn.commit()
    conn.close()

# job_data has "format", add



