FROM python:3.9

RUN pip install pixivpy
RUN pip install Flask
RUN pip install gunicorn

COPY ./pixiv.py .

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "pixiv:app"]