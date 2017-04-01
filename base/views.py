# coding: utf-8

"""
    base.views
    ~~~~~~~~~~

    The most common views for the whole project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask.templating import render_template
from flask.views import MethodView
from flask import flash, redirect, request, url_for
from flask.ext.login import login_user, login_required, logout_user

from ext import login_manager
from base import base
from base.forms import LoginForm
from base.forms import ScheduleForm
from base.models import User
from base import models
from settings import BaseConfig

class FrontView(MethodView):

    def get(self):
        posts = BaseConfig.SITE_REFERENCES
        events = models.Event.get_promotes(4) #只查詢4筆
        schedules = models.Schedule.get_openning()        
        return render_template(
            'base/main.html', site_title = BaseConfig.SITE_REFERENCES[0], refs = posts, promotes = events, activates = schedules
        )
        
class MemberView(MethodView):
	
    def get(self):
        posts = BaseConfig.SITE_REFERENCES
        events = models.Event.get_promotes(4) #只查詢4筆
        schedules = models.Schedule.get_openning()        
        return render_template(
            'base/member.html', refs = posts, promotes = events, activates = schedules
        )
        
class EventView(MethodView):
	
    def get(self):
        posts = BaseConfig.SITE_REFERENCES
        events = models.Event.get_promotes(4) #只查詢4筆
        schedules = models.Schedule.get_openning()        
        return render_template(
            'base/event.html', refs = posts, promotes = events, activates = schedules
        )
        
class ScheduleView(MethodView):
    _messages = {
        'success': 'You are the boss!',
        'invalid_auth': 'Who are you?',
        'invalid_form': 'Invalid form.',
    }
    
    def get(self):
        id = request.args.get("id")        
        schedule = models.Schedule.get_by_id(id)
        if schedule is not None :
            event = models.Event.get_by_id(schedule.event)
            posts = BaseConfig.SITE_REFERENCES
            return render_template(
                'base/schedule.html', refs = posts, e = event, s = schedule
            )
        else :
            return redirect(url_for('base.front_page'))
            
    def post(self):
        form = ScheduleForm()
        if form.validate_on_submit():			
            return render_template('base/confirm_schedule.html', form=form)
        return redirect(url_for('base.front_page'))

class LoginView(MethodView):
    _messages = {
        'success': 'You are the boss!',
        'invalid_auth': 'Who are you?',
        'invalid_form': 'Invalid form.',
    }

    def get(self):
        return render_template('login.html', form=LoginForm())

    def post(self):
        form = LoginForm()
        if not form.validate_on_submit():
            flash(self._messages['invalid_form'])
            return render_template('login.html', form=form)

        user = User.get_by_email(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(self._messages['success'])
        else:
            flash(self._messages['invalid_auth'])
            return redirect(url_for('base.login'))

        return redirect(request.args.get('next') or url_for('base.front_page'))

login_manager.login_view = 'base.login'
login_manager.login_message = 'You have to log in to access this page.'


class AboutView(MethodView):
	
    def get(self):
        return render_template('base/about.html')


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@login_required
def logout():
    logout_user()
    return redirect(url_for('base.front_page'))

base.add_url_rule('', view_func=FrontView.as_view('front_page'))
base.add_url_rule('event', view_func=EventView.as_view('event_page'))
base.add_url_rule('schedule', view_func=ScheduleView.as_view('schedule_page'))
base.add_url_rule('member', view_func=MemberView.as_view('member_page'))
base.add_url_rule('login', view_func=LoginView.as_view('login'))
base.add_url_rule('logout', view_func=logout, methods=['POST'])
base.add_url_rule('about', view_func=AboutView.as_view('about'))
