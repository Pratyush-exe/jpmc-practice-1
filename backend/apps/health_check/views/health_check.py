from common.views import BaseView


class HealthCheckup(BaseView):
    """Class for health checkup. Used to check if server is up"""

    def get(self):
        return self.get_response(data={"message": "Healthy"})
