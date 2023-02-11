# Django-Ecommerce

This project is an online store. Not a little and not a lot of logic is written on it, of course there are flaws, but in
principle the project is normal. It uses a PostgreSQL database. When adding images to products, they are automatically
sorted inside the media folder by title.

## Installation for Linux

### Python

```bash
  sudo apt-get install python3.10.6
```

### Required libraries for the project

```bash
  sudo pip3 install -r requirements/base.txt
```    

## Installation for Windows

### Python

```bash
  https://www.python.org/downloads/
```

Required libraries for the project

```bash
  pip install -r requirements/base.txt
```    

## Create .env file

Create .env file in root folder for your settings

```bash
# Secret key
SECRET_KEY=YOURSECRETKEY

# Database settings
DATABASE_NAME=YOUR_DATABASE_NAME
DATABASE_USER=YOUR_DATABSE_USER
DATABASE_PASS=YOUR_DATABASE_PASSWORD

# Email settings
EMAIL_HOST_USER=EMAILFORPROJECT
EMAIL_HOST_PASSWORD=EMAILHOSTPASSWORD
```

## Collect static
```bash
python3 manage.py collectstatic
```

## How to Run for Linux

```bash
python3 main.py
```

## How to Run for Windows

```bash
python main.py
```

## Features

- Easier to manage
- No need to open an online diary: kundalik.com
- Without advertising
- Works fast

## Feedback

If you have any feedback, please reach out to us at saidakhmedovsaidalo@gmail.com

## Screenshots

![App Screenshot](https://imgur.com/pGD0PN6.png)

![App Screenshot](https://imgur.com/WbbViHY.png)

If schedule not found:
![App Screenshot](https://imgur.com/sqD7U2D.png)