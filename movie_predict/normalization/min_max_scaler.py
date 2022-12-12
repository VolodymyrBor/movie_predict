import numpy as np


class MinMaxScaler:

    def __init__(
        self,
        min_value: float | None = None,
        max_value: float | None = None,
    ):
        self.max_value = max_value
        self.min_value = min_value

        self._scale_values = np.vectorize(self._scale_value)
        self._restore_values = np.vectorize(self._restore_value)

    def scale(self, array: np.ndarray) -> np.ndarray:
        min_value, max_value = self._find_min_max(array)
        return self._scale_values(array, min_value, max_value)

    def restore(self, array: np.ndarray) -> np.ndarray:
        if self.min_value is None:
            raise ValueError('min_value is None')

        if self.max_value is None:
            raise ValueError('max_value is None')

        return self._restore_values(array, self.min_value, self.max_value)

    def _find_min_max(self, array: np.ndarray) -> tuple[float, float]:
        if self.max_value is None:
            self.max_value = np.amax(array)
        if self.min_value is None:
            self.min_value = np.amin(array)
        return self.min_value, self.max_value

    @staticmethod
    def _scale_value(x: float, min_value: float, max_value: float) -> float:
        return (x - min_value) / (max_value - min_value)

    @staticmethod
    def _restore_value(scaled: float, min_value: float, max_value: float) -> float:
        return scaled * (max_value - min_value) + min_value
