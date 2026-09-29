import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def login_user(email, password):
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    if not response.session:
        raise ValueError("Login failed")

    return {
        "access_token": response.session.access_token,
        "user_id": response.user.id,
        "email": response.user.email
    }


def get_current_user(token):
    response = supabase.auth.get_user(token)

    if not response.user:
        raise ValueError("Invalid or expired token")

    return response.user