ALL_FILE_EVENTS = {
    "event_filter": {
        "file_events": [
            {"type": "FILE_EVENT_TYPE_OPEN"}
        ]
    }
}

ALL_PROCESS_EVENTS = {
    "event_filter": {
        "process_events": [
            {"type": "PROCESS_EVENT_TYPE_FORK"},
            {"type": "PROCESS_EVENT_TYPE_EXEC"},
            {"type": "PROCESS_EVENT_TYPE_EXIT"},
            {"type": "PROCESS_EVENT_TYPE_UPDATE"},
        ]
    }
}

ALL_CONTAINER_EVENTS = {
    "event_filter": {
        "container_events": [
            {"type": "CONTAINER_EVENT_TYPE_CREATED"},
            {"type": "CONTAINER_EVENT_TYPE_RUNNING"},
            {"type": "CONTAINER_EVENT_TYPE_EXITED"},
            {"type": "CONTAINER_EVENT_TYPE_DESTROYED"},
            {"type": "CONTAINER_EVENT_TYPE_UPDATED"}
        ]
    }
}

ALL_EVENTS = {
    'event_filter': {
        'process_events': [{'type': 'PROCESS_EVENT_TYPE_FORK'},
                           {'type': 'PROCESS_EVENT_TYPE_EXEC'},
                           {'type': 'PROCESS_EVENT_TYPE_EXIT'}],
        'container_events': [{'type': 'CONTAINER_EVENT_TYPE_CREATED'},
                             {'type': 'CONTAINER_EVENT_TYPE_RUNNING'},
                             {'type': 'CONTAINER_EVENT_TYPE_EXITED'},
                             {'type': 'CONTAINER_EVENT_TYPE_DESTROYED'}],
        'file_events': [{'type': 'FILE_EVENT_TYPE_OPEN'}]
    }
}


def syscall_events(*syscall_ids, include_exit=False):
    return {
        'event_filter': {
            'syscall_events': [{"type": "SYSCALL_EVENT_TYPE_ENTER", "id": {"value": id}} for id in syscall_ids] if not include_exit else [{"type": "SYSCALL_EVENT_TYPE_ENTER", "id": {"value": id}} for id in syscall_ids] + [{"type": "SYSCALL_EVENT_TYPE_EXIT", "id": {"value": id}} for id in syscall_ids]
        }
    }
