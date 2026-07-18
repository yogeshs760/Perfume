import requests

def download_video(url, output_filename="video.mp4"):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            # 'wb' yaani Write Binary mode
            with open(output_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print("Video kamyabi se download ho gayi hai!")
        else:
            print(f"Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Use karne ke liye:
download_video("Aapka_Video_URL_Yahan")