from django.urls import path

# SHOW IN JSON
from todolist.views import show_json
# ADD TASK IN JSON
from todolist.views import add_task

# REGISTER
from todolist.views import register
# LOGIN
from todolist.views import login_user
# LOGOUT
from todolist.views import logout_user

# HOME
from todolist.views import show_todolist
# NEW TASK
from todolist.views import new_task
# REMOVE TASK
from todolist.views import remove_task
# CHANGE TASK STATUS
from todolist.views import status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),

    # SHOW IN JSON
    path('json/', show_json, name='show_json'),
    # ADD IN JSON
    path('add', add_task, name= 'add_task'),
    
    # REGISTER
    path('register/', register, name='register'),
    # LOGIN
    path('login/', login_user, name='login'),
    # LOGOUT
    path('logout/', logout_user, name='logout'),
    # NEW TASK
    path('create-task/', new_task, name='new_task'),
    # DELETE TASK
    path('remove-task/<int:id>', remove_task, name='remove_task'),
    # CHANGE TASK STATUS
    path('task-status/<int:id>', status, name='status')
]