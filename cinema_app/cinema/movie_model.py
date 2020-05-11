class MovieModel:
    def __init__(self, *, m_id, name, rating):
        self.id = m_id
        self.name = name
        self.rating = rating

    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements

    def validate_movie(self, movie):
        if movie is None:
            raise Exception("Movie is not found.")
