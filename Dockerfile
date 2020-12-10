FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install flask pytz

ENV FLASK_APP mock_partner_transaction.py
ENV FLASK_ENV development

CMD ["flask", "run", "--debugger", "--with-threads", "--host", "0.0.0.0"]
