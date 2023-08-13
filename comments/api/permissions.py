from rest_framework.permissions import BasePermission
from ..models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    # Solo al autor del comentario puede modificar borrar
    def has_permission(self,request,view):
        # Obtener y crear no necesitan permisos
        if request.method == 'GET' or request.method == 'POST':
            return True 
        else:
            # obtenemos id del comentario
            id_comment = view.kwargs['pk']
            # obtenemos data del comentario
            comment = Comment.objects.get(pk=id_comment)
            # obtenemos el id del user que está realizando la petición
            id_user = request.user.pk
            # obtenemos el id del user que ha creado el comentario
            id_user_comment = comment.author_id
            # comparamos id_user y id_user_comment
            if id_user == id_user_comment:
                return True
            
            return False
            