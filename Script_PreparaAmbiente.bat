echo "
python manage.py migrate --fake-initial
python manage.py shell
from django.contrib.auth.models import User; User.objects.create_superuser('theo.krejci','atelie.modaintima@gmail.com', 'theo.krejci')


from portal.models import Pais, Estado, Cidade , Instituicao

pais = Pais.objects.create(nome = 'BRASIL', abreviacao = 'BRA', stativo = '1')

exit()
python manage.py runserver
" 