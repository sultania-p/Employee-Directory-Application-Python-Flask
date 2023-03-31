# storing standard roots page - landing page, home etc.

from flask import Blueprint, render_template
from flask_login import current_user, login_required


views  = Blueprint('views', __name__)

# define the roots or views
@views.route('/')
@login_required
def home():
    return render_template("home.html")
