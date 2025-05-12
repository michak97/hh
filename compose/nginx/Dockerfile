FROM ubuntu:20.04

RUN apt-get update \
    && apt-get -y dist-upgrade \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        nginx-extras \
        libnginx-mod-http-lua \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Kopiere nginx-Konfiguration
ADD nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/.htpasswd

COPY *.key /etc/ssl/private/
COPY *.cer /etc/ssl/certs/

ARG HTTP_AUTH_LOGIN
ARG HTTP_AUTH_PASSWORD

RUN echo -n $HTTP_AUTH_LOGIN:$(openssl passwd -apr1 $HTTP_AUTH_PASSWORD) >> /etc/nginx/.htpasswd

RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

CMD ["nginx", "-g", "daemon off;"]
