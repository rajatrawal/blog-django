# Blog Website

[![GitHub Repository](https://img.shields.io/badge/GitHub%20Repo-Blog%20Website-green)](https://github.com/rajatrawal/blog-django)
[![Render Deployment](https://img.shields.io/badge/Deployment-Render-orange)](https://django-blog-npsy.onrender.com/)

[![Django](https://img.shields.io/badge/Django-Backend-blue)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-Styling-blue)](https://getbootstrap.com/)

📝 Welcome to the Blog Website! This Django-based application allows users to read and comment on blogs created by the administrator. Users can also reply to comments, fostering a community-driven discussion platform. The application is deployed on the Render cloud platform.

## Features

1. **Blog Reading**: Users can read blogs posted by the administrator.

2. **Comments and Replies**: Users can leave comments on blogs, and also reply to existing comments.

3. **Admin Panel**: Administrators can manage blogs, comments, and replies via the Django admin panel.

## Preview
![Capture](https://github.com/rajatrawal/blog-django/assets/72153827/ea82c671-4622-4b37-b95e-bff77278b8af)


## Usage

1. Explore the live demo of the Blog Website [here](https://django-blog-npsy.onrender.com/).

2. Read blogs, leave comments, and engage in discussions.

3. Administrators can access the admin panel using the credentials `admin` (username) and `admin` (password).

## Installation

To run this project locally for development purposes, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/rajatrawal/blog-django.git
   ```

2. Navigate to the project directory:

   ```shell
   cd blog-django
   ```

3. Install dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```shell
   python manage.py migrate
   ```

5. Create a superuser for admin access:

   ```shell
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Open your web browser and explore the project locally at [http://localhost:8000/](http://localhost:8000/).

## Tech Stack

- **Django**: Backend framework for building robust web applications.

- **Bootstrap**: Frontend framework for responsive and attractive styling.

## Contribute

If you'd like to contribute to this project, have suggestions for improvement, or wish to add more features, please feel free to submit issues or pull requests on [GitHub](https://github.com/rajatrawal/blog-django). Your contributions are appreciated! 🚀

Thank you for using the Blog Website. Happy reading and commenting! 📖💬
