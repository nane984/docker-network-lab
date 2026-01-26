FROM postgres:16-alpine

RUN apk add --no-cache bash tzdata

WORKDIR /

COPY backup_postgres.sh /backup_postgres.sh
COPY crontab.txt /etc/crontabs/root

RUN chmod +x /backup_postgres.sh

CMD ["crond", "-f", "-l", "2"]