import requests

def fetch_remoteok_jobs():

    url = "https://remoteok.io/api"
    headers = {
        "User-Agent": "JobFetcherBot/1.0 (elena.mikhaleva56@gmail.com)",
        "Accept": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        jobs = data[1:]

        for job in jobs:
            searchable_text = f"{job.get('position', '')} {job.get('company', '')} {job.get('location', '')} {' '.join(job.get('tags', []))}".lower()
            print(f"Position: {job.get('position')}")
            print(f"Company: {job.get('company')}")
            print(f"Location: {job.get('location')}")
            print(f"Tags: {job.get('tags')}")
            print(f"URL: {job.get('url')}")
            print("-" * 10)

        return jobs
    else:
        print(f"Failed to fetch jobs: HTTP {response.status_code}")

if __name__ == "__main__":
    fetch_remoteok_jobs()