import scraping
import schedule
import time

#download covid data once a day at 7pm
def job():
    scraping.download_and_extract_csv()

schedule.every().day.at('19:00').do(job)
print('Scheduler started. Press Ctrl+C to stop.')

while True:
    schedule.run_pending()
    time.sleep(1)
