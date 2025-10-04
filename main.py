
from src.db.schema import *

if __name__ == '__main__':
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE job_ads
        ADD FOREIGN KEY (JobNormalized) REFERENCE jobs_normal(ID)
        """)
    conn.commit()
    conn.close()
    print("table is modified.")


