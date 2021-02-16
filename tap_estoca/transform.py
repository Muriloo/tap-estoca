import singer


def transform(transformer, record, stream_schema, stream_metadata):

    xf_record = _xf_replace_none(record)
    transformed_record = transformer.transform(xf_record, stream_schema, stream_metadata)
    return transformed_record


def _xf_replace_none(record):
    """Handles when the API returns 'None' as a string instead of null."""
    
    xf_record = dict()
    for key, value in record.items():
        if value == 'None':
            xf_record[key] = None
        else:
            xf_record[key] = value
    
    return xf_record
