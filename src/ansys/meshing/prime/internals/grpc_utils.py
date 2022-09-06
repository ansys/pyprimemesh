import ansys.meshing.prime.internals.defaults as defaults


def get_default_channel_args():
    return [
        # ('grpc.keepalive_time_ms', 60000), # 1 minute
        ('grpc.keepalive_timeout_ms', 10000),  # 10 seconds
        ('grpc.keepalive_permit_without_calls', True),
        ('grpc.http2.max_pings_without_data', 0),  # Disable
        ('grpc.max_send_message_length', defaults.max_message_length()),
        ('grpc.max_receive_message_length', defaults.max_message_length()),
    ]
