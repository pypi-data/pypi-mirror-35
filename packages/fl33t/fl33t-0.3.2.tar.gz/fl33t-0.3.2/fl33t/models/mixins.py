"""
Mixins

Reusable pieces for Fl33t models
"""


class ManyDevicesMixin:  # pylint: disable=too-few-public-methods
    """For models with child devices"""
    def devices(self):
        """Return the child devices"""
        return self._client.list_devices(fleet_id=self.fleet_id)


class ManyBuildsMixin:  # pylint: disable=too-few-public-methods
    """For models with child builds"""
    def builds(self):
        """Return the child builds"""
        return self._client.list_builds(train_id=self.train_id)


class OneBuildMixin:  # pylint: disable=too-few-public-methods
    """For models with a build parent"""
    def build(self):
        """Return the parent build"""
        return self._client.get_build(self.build_id)


class OneTrainMixin:  # pylint: disable=too-few-public-methods
    """For models with a train parent"""
    def train(self):
        """Return the parent train"""
        return self._client.get_train(self.train_id)


class ManyFleetsMixin:  # pylint: disable=too-few-public-methods
    """For models with child fleets"""
    def fleets(self):
        """Return the child fleets"""
        return self._client.list_fleets(train_id=self.train_id)


class OneFleetMixin:  # pylint: disable=too-few-public-methods
    """For models with a parent fleet"""
    def fleet(self):
        """Return the parent fleet"""
        return self._client.get_fleet(self.fleet_id)
