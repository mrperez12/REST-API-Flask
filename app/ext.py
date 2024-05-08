# Este fichero lo utilizaremos para instanciar las distintas extensiones
# que utilicemos en la aplicacion para evitar referencias circulares.
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

ma = Marshmallow()
migrate = Migrate()