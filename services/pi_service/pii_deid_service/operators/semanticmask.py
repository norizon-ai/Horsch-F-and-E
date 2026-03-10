from presidio_anonymizer.operators import Operator, OperatorType

class Semanticmask(Operator):
    def operate(self, text: str, params = None) -> str:
        """Masks a given text with a given entity matching mask.

        :param text: the text to be masked
        :param params:
            clusters: dictionary, entries are the plain text and will be replaced by keys
        :return: the masked text
        """

        clusters = params.get("clusters")
        for key, value in clusters.items():
            for item in value:
                if item == text:
                    return f"<{key.split(' ')[0].upper()}_{key.split(' ')[1]}>"
        return "???"

    def validate(self, params = None) -> None:
        """Validate each operator parameters."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "semanticmask"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize