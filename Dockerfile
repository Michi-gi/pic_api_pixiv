FROM python:3.9

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
  echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update -y
RUN apt-get install -y vim
RUN apt-get install -y unzip
RUN apt-get install -y google-chrome-stable

RUN wget -qO /tmp/chromedriver.zip \
    "http://chromedriver.storage.googleapis.com/$(wget -qO- chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip" \
    && unzip -qq /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN pip install gppt
RUN pip install pixivpy
RUN pip install Flask
RUN pip install gunicorn

COPY ./pixiv.py .

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "pixiv:app"]