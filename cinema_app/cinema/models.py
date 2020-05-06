class MoveModel:
    def __init__(self, *, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements

    def validate_movie(self, movie):
        if movie is None:
            raise Exception("Movie is not found.")
