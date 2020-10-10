FROM rackspacedot/python37

RUN pip3 install tornado

COPY double-vortex.html .
COPY double-vortex.js .
COPY main.py .

CMD ["python3", "main.py"]
