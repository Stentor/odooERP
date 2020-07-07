FROM opaconsulting/odoo13-master
COPY ./addons /mnt/extra-addons
COPY ./odoo.conf /etc/odoo/odoo.conf

