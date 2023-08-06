import logging
import uuid

logger = logging.getLogger(__name__)


def init_from_config(conf):
    id_ = conf.general.get('cluster_id')
    if id_ is None:
        id_ = uuid.uuid4().hex
        logger.info('Setting Cluster ID to %s', id_)
        conf.general.cluster_id = id_
        conf.general.save()
