📱 Social Media Feed – Django Project

A simple but functional social media feed built using Django, featuring:

User Signup & Login

User Profile with Picture, DOB & Address

Create Posts (with Images)

Like / Unlike System

Comment System

View Liked Posts

Search Users

Profile Page with Post History

Username Update

Guest User Feed (view only)

This project is beginner-friendly and follows clean and modular Django practices.

🚀 Features
👤 User Authentication

Signup with username, email, password

Upload profile picture during signup

Add date of birth & address

Login / Logout

📄 User Profile

Display profile photo

Show date of birth & address

List user posts

Show liked posts

Username change option

📝 Post System

Create posts (text + image)

Delete own posts

Feed showing newest posts first

❤️ Like System

Like or Unlike any post

View all posts liked by the user

💬 Comments

Add comments

Delete own comments

🔍 Search Users

Search users by username or name

🏗️ Project Structure
core/
├── models.py
├── views.py
├── forms.py
├── signals.py
├── urls.py
├── templates/
social_media_feed/
├── settings.py
├── urls.py
media/
static/

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/social-media-django.git
cd social-media-django

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the server
python manage.py runserver

🖼️ Profile Creation Using Signals

A Django signal automatically creates a Profile whenever a new User is created.

File: core/signals.py

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


This ensures every user always has a profile.

📷 Media & Static Files

User-uploaded images (post images & profile pictures) are stored in:

/media/


Add these settings to settings.py:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

🎨 Frontend

This project uses:

Bootstrap 5

Responsive, clean UI

Simple, minimal layout

🧪 Future Improvements (Optional)

Password reset & email OTP

Follow/Unfollow system

Notifications

Dark mode

Real-time chat system (WebSockets)

Deployment on Render / Railway

🤝 Contributing

Feel free to open issues or submit pull requests!

📄 License

This project is licensed under the MIT License.