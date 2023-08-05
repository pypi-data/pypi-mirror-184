from vsp_model_insight.common.protocol import BaseObject


def process_options(options):
    code_cs = parse_connection_string(options.connection_string)
    options.table_name = code_cs.get('table_name')
    options.endpoint = code_cs.get('endpoint')
    options.sas_token = code_cs.get('sas_token')


def parse_connection_string(connection_string: str):
    if connection_string is None:
        return {}
    try:
        rev_con = connection_string[::-1]
        end_point_last_index = len(rev_con) - rev_con.index("/") - 1
        end_point = connection_string[0:end_point_last_index]
        sas_token = connection_string[connection_string.index("?"):]
        table_name = connection_string[end_point_last_index +
                                       1:connection_string.index("?")]
        result = {'endpoint': end_point,
                  'sas_token': sas_token, 'table_name': table_name}
    except Exception:
        raise ValueError('Invalid connection string')
    return result


class Options(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Options, self).__init__(*args, **kwargs)
        process_options(self)

    _default = BaseObject(
        connection_string=None,
        table_name=None,
        endpoint=None,
        sas_token=None,
        # enable_local_storage=False,
        export_interval=15.0,
        grace_period=5.0,
        logging_sampling_rate=1.0,
        max_batch_size=25,
        queue_capacity=8192,
    )
