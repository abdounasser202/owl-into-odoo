# Odoo14

This is an Odoo 14 docker environment

## Installation

```
docker-compose up
docker-compose exec odoo bash
odoo -i base -d odoo --stop-after-init --db_host=db -r odoo -w odoo
```