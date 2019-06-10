class BaseModelView(ModelView):
    permission_name = ''

    def is_accessible(self):
        return True
        # return current_user.is_authenticated and (current_user.user['is_admin'] or self.permission_name in get_user_permissions(current_user.user))

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('user.login', next=request.url))