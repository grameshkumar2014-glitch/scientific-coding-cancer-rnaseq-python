def validate_inputs(counts, metadata):
    assert counts.shape[1] == metadata.shape[0], "Sample mismatch detected"