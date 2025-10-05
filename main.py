from src.backend.db.schema import *
from src.backend.parser_hh import *


def tables_drop_create():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS job_ads")
    conn.commit()
    cursor.execute("DROP TABLE IF EXISTS skills")
    conn.commit()
    cursor.execute("DROP TABLE IF EXISTS link_jobad_skill")
    conn.commit()
    cursor.execute("DROP TABLE IF EXISTS jobs_normal")
    conn.commit()
    conn.close()
    create_skills_table()
    create_jobad_skill_table()
    create_job_ads_table()
    create_formats_table()
    create_jobad_format_table()


if __name__ == '__main__':
    # tables_drop_create()
    fetch_hh_jobs(query="qa", pages=1)
    print("done")

