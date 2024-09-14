from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user

from .models.event import Event

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
@login_required
def home():
    events = Event.find_by_user_id(current_user.id)

    return render_template("home.html", user=current_user, events=events)

@routes.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    if request.method == "POST":
        name = request.form.get('event_name')
        description = request.form.get('description')
        date = request.form.get('date')
        time = request.form.get('time')
        place = request.form.get('place')
        type = request.form.get('type')
        user_id = current_user.id

        Event.create_event(name, description, date, time, place, type, user_id)
        flash('Event created successfully!', category='success')
        return redirect(url_for('routes.home'))
          
    return render_template("create_event.html", user=current_user)