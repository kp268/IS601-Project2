FROM python:3

ADD . .

RUN pip install coverage numpy

CMD [ "python", "-m","unittest", "discover", "-s", "Tests" ]
