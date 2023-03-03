from uuid import UUID

from abstract_base_repository import AbstractBaseRepository

class DjangoRepository(AbstractBaseRepository):
    PAGE_SIZE = 25
    __django_model__ = None
    __domain_model__ = None

    def list(self, page=0):
        return [entity.to_domain()
                for entity in self.__django_model__.objects.all()[
                page * self.PAGE_SIZE: (page * self.PAGE_SIZE) + self.PAGE_SIZE]]

    def get(self, id: UUID):
        try:
            return self.__django_model__.objects.get(id=id).to_domain()
        except self.__django_model__.DoesNotExist:
            return None

    def add(self, entity):
        self.__django_model__(**entity.__dict__).save()

    def update(self, entity):
        entity_under_change = self.__django_model__.objects.get(id=entity.id)
        for attribute in [x for x in entity_under_change.__dict__ if x != '_state']:
            setattr(entity_under_change, attribute, entity.__dict__[attribute])
        entity_under_change.save()

    def delete(self, id: UUID):
        self.__django_model__.objects.get(id).delete()

    def count(self) -> int:
        return self.__django_model__.objects.count()

    def all(self):
        return [x.to_domain() for x in self.__django_model__.objects.all()]

    def __len__(self):
        return self.count()

    def __getitem__(self, item: UUID):
        return self.get(item)
