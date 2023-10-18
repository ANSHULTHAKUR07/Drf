from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        # if view.action == 'create':
        #     return True
        # else:
        #     return request.user.is_authenticated
        # print(request.method)
        if request.method == 'POST':
            print("in request method")
            return True
        else:
            print("in else :")
            return request.user.is_authenticated