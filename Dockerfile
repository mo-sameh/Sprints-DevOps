FROM python:3.8-alpine
WORKDIR /var/src/app
LABEL org.opencontainers.image.authors="Moahmed Sameh"
RUN mkdir Sprints_DevOps
COPY sprints.py Sprints_DevOps/
COPY test.py Sprints_DevOps/
COPY sshd.sh Sprints_DevOps/
