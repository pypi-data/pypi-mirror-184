from assimilator.alchemy.database import AlchemyRepository as BaseAlchemyRepository
from assimilator.core.database.exceptions import NotFoundError


class AlchemyRepository(BaseAlchemyRepository):
    def delete(self, obj):
        if obj.is_removed:
            raise NotFoundError()

        obj.is_removed = True
