FROM python

WORKDIR /drf-api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_MANAGEPY_MIGRATE=true

CMD ["./entrypoint.sh"]
