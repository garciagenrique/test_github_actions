FROM docker.io/python:3.8-slim

SHELL [ "/bin/bash", "-c"]

RUN apt update
COPY . test_github_actions
RUN pip install "./test_github_actions"
RUN rm -rf test_github_actions

ENTRYPOINT /bin/bash
