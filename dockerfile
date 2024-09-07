# 使用官方的 Python 運行時作為基礎映像
FROM python:3.10

# 設置容器內的工作目錄
WORKDIR /app

# 複製當前目錄下的內容到容器中的 /app 目錄
COPY . /app

# 安裝 requirements.txt 中指定的依賴
RUN pip install --no-cache-dir -r requirements.txt

# 對外開放 80 端口
EXPOSE 8000

# 運行 uvicorn 服務器
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]