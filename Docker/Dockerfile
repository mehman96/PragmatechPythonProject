WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

CMD [ "flask", "run"]
