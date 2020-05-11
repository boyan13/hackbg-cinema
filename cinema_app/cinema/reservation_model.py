class ReservationModel:
    def __init__(self, *, r_id, u_id, pr_id):
        self.id = r_id
        self.pr_id = pr_id
        self.u_id = u_id

    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements
