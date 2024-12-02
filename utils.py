import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class DataUtils:
    @staticmethod
    def convert_to_float(value: str) -> float:
        try:
            return round(float(value), 2)
        except ValueError as e:
            logging.error(f"Erreur de conversion pour la valeur '{value}': {e}")
            raise ValueError(f"La valeur '{value}' n'est pas un nombre valide.")

    @staticmethod
    def retrieve_percent_from_string(value: str):
        return value.replace("%", "")
