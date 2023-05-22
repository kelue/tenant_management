## Tenant Management System

The tenant management system is designed to streamline and automate various tasks related to managing tenants in a residential or commercial property setting. Built with Frappe framework, a low-code frame utilizing javascript and python with batteries included for fast development of web applications.

To run the application in local, install frappe-bench in your local using

```linux
  sudo apt install frappe-bench
```
see detailed installtion instructions [here](https://frappeframework.com/docs/v14/user/en/installation)

Initialise a frappe-bench directory using the bench cli
```linux
  bench init [folder-name] && cd [folder-name]
```
Create a site to run frappe applications. See instructions [here](https://frappeframework.com/docs/v14/user/en/tutorial/create-a-site)

then get the app from this repo
```linux
  bench get-app https://github.com/kelue/tenant_management.git
```

## requirements

```
Python 3.10+ (v14)
Node.js 16
Redis 6                                       (caching and realtime updates)
MariaDB 10.6.6+ / Postgres v12 to v14         (Database backend)
yarn 1.12+                                    (js dependency manager)
pip 20+                                       (py dependency manager)
wkhtmltopdf (version 0.12.5 with patched qt)  (for pdf generation)
cron                                          (bench's scheduled jobs: automated certificate renewal, scheduled backups)
NGINX                                         (proxying multitenant sites in production)
```

#### License

MIT
