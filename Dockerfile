# 使用支持CUDA的基础镜像
FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

# 设置工作目录
WORKDIR /app

# 安装基本依赖
RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 复制requirements文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码
COPY . .

# 设置环境变量
ENV PYTHONPATH=/app
ENV OPENAI_API_KEY="your_api_key_here"