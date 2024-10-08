import requests
from datetime import datetime

def get_prayer_times(latitude, longitude, method=2):
    
    url = f"https://api.aladhan.com/v1/timings/{datetime.now().date()}?latitude={latitude}&longitude={longitude}&method={method}"
    response = requests.get(url)
    data = response.json()
    return data['data']['timings']

if __name__ == "__main__":
    latitude =  28.63576000  # Latitude of Delhi
    longitude = 77.22445000  # Longitude of Delhi

    prayer_times = get_prayer_times(latitude, longitude)

    print("Salah Timings for Today:")
    print("Fajr:", prayer_times['Fajr'])
    print("Dhuhr:", prayer_times['Dhuhr'])
    print("Asr:", prayer_times['Asr'])
    print("Maghrib:", prayer_times['Maghrib'])
    print("Isha:", prayer_times['Isha'])
