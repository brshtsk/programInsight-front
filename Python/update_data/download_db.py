import requests
from utils import Utils


class Downloader:
    @staticmethod
    def download_from_source_url(output_path):
        with open(Utils.resource_path('Python/source_url.txt'), 'r') as f:
            source_url = f.read().strip()
        if source_url.startswith('https://github.com'):
            Downloader.download_from_github(source_url, output_path)
        if source_url.startswith('https://disk.yandex.ru/'):
            Downloader.download_from_yadisk(source_url, output_path)

    @staticmethod
    def download_from_github(share_url, output_path):
        share_url = share_url.replace('github.com', 'raw.githubusercontent.com').replace('blob/', '')
        r = requests.get(share_url)
        with open(output_path, 'wb') as f:
            f.write(r.content)

    @staticmethod
    def download_from_yadisk(share_url, output_path):
        response = requests.get(
            'https://cloud-api.yandex.net/v1/disk/public/resources/download',
            params={'public_key': share_url}
        )

        download_url = response.json()['href']
        r = requests.get(download_url)
        with open(output_path, 'wb') as f:
            f.write(r.content)
