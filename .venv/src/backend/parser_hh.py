import requests
from src.backend.db.data_management import *

def fetch_full_description(vacancy_id):
    url = f"https://api.hh.ru/vacancies/{vacancy_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("description", "")
    return ""

def fetch_hh_jobs(query="qa", area=40, pages=1):
    # area=40 - Kazakhstan
    url = "https://api.hh.ru/vacancies"

    for page in range(pages):
        params = {"text": query, "area": area, "page": page}
        response = requests.get(url, params=params)
        data = response.json()
        # print(data)
        for item in data["items"]:
            description = fetch_full_description(item["id"])
            print(description)
            job_data = {
                "title_raw": item["name"],
                "company": item["employer"]["name"] if item.get("employer") else "",
                "location": item["area"]["name"],
                "format": item["work_format"],
                "salary": item["salary"],
                "url": item["alternate_url"],
                "date_posted": item["published_at"][:10],
                "source": "hh.kz"
            }

            if item["schedule"]["id"]=='fullDay':
                job_data["schedule"] = "Full day"
            else: job_data["schedule"] = "Unknown index"

            if item["experience"]["id"]=='noExperience':
                job_data["experience"] = 0
            else: job_data["experience"] = -1

            print(job_data)
            insert_job_ad(job_data, description)
        print(f"Page {page + 1} done")
    print("All pages inserted!")
