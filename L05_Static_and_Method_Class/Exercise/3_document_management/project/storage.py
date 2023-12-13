from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        return document

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)




# Upon initialization, the class Storage will not receive any parameters.
# It should have 3 instance attributes: categories (empty list), topics (empty list),
# and documents (empty list). The class should have the following methods:
#     • add_category(category: Category) - add the category if it is not in the list
#     • add_topic(topic: Topic) - add the topic if it does not exist
#     • add_document(document: Document) - add the document if it does not exist
#     • edit_category(category_id: int, new_name: str) - edit the name of the category with the provided id
#     • edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) - edit the topic with the given id
#     • edit_document(document_id: int, new_file_name: str) - edit the document with the given id
#     • delete_category(category_id) - delete the category with the provided id
#     • delete_topic(topic_id) - delete the topic with the provided id
#     • delete_document(document_id) - delete the document with the provided id
#     • get_document(document_id) - return the document with the provided id
#     • __repr__() - returns a string representation of each document on separate lines
