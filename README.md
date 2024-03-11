# member_manager

member_manager is a Django web application that allows users to manage team members, including viewing, adding, editing, and deleting team member information.

## Getting Started

These instructions will get you up and running on your local machine. Let's go!

### Prerequisites

Before you begin, ensure you have Python installed on your system. This project was developed with Python 3.12.2, but it should be compatible with any Python 3.x version. You can download Python [here](https://www.python.org/downloads/).

### Setting Up a Virtual Environment

It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects separate by creating isolated environments for them.

1. Install virtualenv if you haven't installed it yet:

```bash
pip install virtualenv
```

2. Navigate to the project directory and create a virtual environment:

```bash
virtualenv venv
```

3. Activate the virtual environment:

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
.\venv\Scripts\activate
```

### Installing Dependencies

With your virtual environment activated, install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### Environment Variables: `.env` file

We use a `.env` file to store values we do not want to check into version control. 

In this app, our only environment variable is Django's [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY)

1. Create a `.env` file at the root of the project with the following contents:
   - ```plaintext
     SECRET_KEY=your_secret_key_here
     ```

2. Replace `your_secret_key_here` with your own secret key. You can generate one with:
   - `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

[Read more about generating Django secret keys here.](https://humberto.io/blog/tldr-generate-django-secret-key/)

### Database Setup

Before running the application, you'll need to apply migrations to set up your database schema:

```bash
python manage.py migrate
```
It will default to using SQLite, so no need to worry about any other database setup.

### Creating a Superuser

To access the Django admin site, you need to create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser.

### Running the Application

To start the development server, run:

```bash
python manage.py runserver
```

The application will be available at [http://localhost:8000](http://localhost:8000).

### Accessing the Admin Site

You can access the Django admin site at [http://localhost:8000/admin](http://localhost:8000/admin) using the superuser credentials you created.

### Code Formatting

For automatic code formatting, we use the following tools:
- Python/General: [black](https://github.com/psf/black)
  - [black VSCode Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- Django HTML Templates: [djLint](https://github.com/djlint/djlint)
  - [djLint VSCode Extension](https://marketplace.visualstudio.com/items?itemName=monosans.djlint)

If you cannot setup your personal code editor to automatically use these, you can choose to use the CLIs.

### Enjoy!

:-)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
