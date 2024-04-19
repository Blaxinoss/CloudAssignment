FROM python:3.9.19-alpine3.19


RUN pip install --no-cache-dir nltk

WORKDIR /app

COPY CloudAssignment2.py random_paragraphs.txt ./

RUN python -m nltk.downloader stopwords

CMD ["python", "CloudAssignment2.py"]

