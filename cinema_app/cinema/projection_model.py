class ProjectionModel:
    def __init__(self, *, pr_id, m_id, pr_date, pr_time):
        self.id = pr_id
        self.m_id = m_id
        self.pr_date = pr_date
        self.pr_time = pr_time

    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements
