"""GDN data connector target for Macrometa GDN collections."""
import pkg_resources
from c8connector import C8Connector, Sample, ConfigAttributeType, Schema
from c8connector import ConfigProperty


class GDNCollectionTargetConnector(C8Connector):
    """GDNCollectionTargetConnector's C8Connector impl."""

    def name(self) -> str:
        """Returns the name of the connector."""
        return "collection"

    def package_name(self) -> str:
        """Returns the package name of the connector (i.e. PyPi package name)."""
        return "macrometa-target-collection"

    def version(self) -> str:
        """Returns the version of the connector."""
        return pkg_resources.get_distribution('macrometa_target_collection').version

    def type(self) -> str:
        """Returns the type of the connector."""
        return "target"

    def description(self) -> str:
        """Returns the description of the connector."""
        return "Data connector source for GDN Collections"

    def validate(self, integration: dict) -> None:
        """Validate given configurations against the connector.
        If invalid, throw an exception with the cause.
        """
        pass

    def samples(self, integration: dict) -> list[Sample]:
        """Fetch sample data using the given configurations."""
        return []

    def schemas(self, integration: dict) -> list[Schema]:
        """Get supported schemas using the given configurations."""
        return []

    def config(self) -> list[ConfigProperty]:
        """Get configuration parameters for the connector."""
        return [
            ConfigProperty('region', ConfigAttributeType.STRING, True, False,
                           description="Fully qualified region URL.", example="api-sample-ap-west.eng.macrometa.io"),
            ConfigProperty('api_key', ConfigAttributeType.STRING, True, False,
                           description="API key.", example="dmi.yzpqqc8DmmdN4adferwe32aN9msnlulMr3sijJGt0..."),
            ConfigProperty('fabric', ConfigAttributeType.STRING, True, False,
                           description="Fabric name.", example="_system"),
            ConfigProperty('target_collection', ConfigAttributeType.STRING, True, True,
                           description="Target collection name", example="SampleCollection"),
            ConfigProperty('batch_size_rows', ConfigAttributeType.INT, False, False,
                           description='Maximum number of rows in each batch. At the end of each batch, '
                                       'the rows in the batch are inserted into the collection.',
                           example='50'),
            ConfigProperty('batch_flush_interval', ConfigAttributeType.INT, False, False,
                           description='Time interval between batch flush task executions in seconds.',
                           example='60'),
            ConfigProperty('batch_flush_min_time_gap', ConfigAttributeType.INT, False, False,
                           description='Minimum time gap between two batch flush tasks in seconds.',
                           example='120'),
        ]

    def capabilities(self) -> list[str]:
        """Return the capabilities[1] of the connector.
        [1] https://docs.meltano.com/contribute/plugins#how-to-test-a-tap
        """
        return []
