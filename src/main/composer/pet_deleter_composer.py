from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.pet_deleter_view import PetDeleterView

def pet_deleter_composer():
    repository = PetsRepository(db_connection_handler)
    controller = PetDeleterController(repository)
    view = PetDeleterView(controller)
    
    return view
