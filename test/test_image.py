from PIL import Image

keyword = "비트코인"
from datetime import datetime

now = datetime.now()
formatteed_date = now.strftime("%y%m%d")

# 이미지 파일 경로
image_path = f"./graph/{formatteed_date}/{keyword}_graph.png"

# 이미지 로드
image = Image.open(image_path)

# 이미지 표시
image.show()
