from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument('start-maximized')

upload_video('tiktok/test.mp4',
            description='this is my description',
            cookies='tiktok/cookies.txt')