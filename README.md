# Social Media Platform

A full-stack **Django + HTML/CSS/JavaScript** social media platform with user authentication, profiles, posts, and social interactions. A comprehensive web application for sharing content and connecting with others.

## Overview

Social Media Platform is a modern web application built with Django and vanilla HTML/CSS/JavaScript. It provides users with a feature-rich social networking experience including user profiles, post creation and sharing, social interactions (likes, comments), and user search functionality.

## Features

- User authentication with secure login/signup
- User profiles with customizable bio and profile pictures
- Create, edit, and delete posts
- Like posts and add comments
- Follow/unfollow other users
- Search and discover users
- Responsive mobile-friendly design
- Real-time feed updates

## Tech Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite/PostgreSQL
- **Template Engine**: Django Jinja2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ritvikvr/social-mediaPlatform.git
cd social-mediaPlatform
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Usage

- Navigate to `http://localhost:8000/` to access the application
- Sign up for a new account or login
- Complete your profile
- Search for users to follow
- Create posts and interact with other users' posts
- Access admin panel at `http://localhost:8000/admin/`

## Project Structure

- `manage.py` - Django management script
- `social_platform/` - Main project configuration
- `app/` - Main Django application with models, views, and forms
- `templates/` - HTML templates (login, signup, profile, feed, etc.)
- `static/` - Static files (CSS, JavaScript, images)

## Database Models

- **User**: Custom user model with profile information
- **Post**: User posts with content and media support
- **Comment**: Comments on posts
- **Follow**: User follow relationships

## Future Enhancements

- Direct messaging
- Notifications system
- Hashtags and trending
- Real-time updates with WebSockets
- Video support
- Mobile app version

## Contributing

Fork the repository, create a feature branch, and submit a pull request.

## License

MIT License - See LICENSE file for details

## Author

**Ritvik Verma** (@ritvikvr)
- GitHub: [https://github.com/ritvikvr](https://github.com/ritvikvr)
- Focus: Full-stack development, Django applications, social platforms
