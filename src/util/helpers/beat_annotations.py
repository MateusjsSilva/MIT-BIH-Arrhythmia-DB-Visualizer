# Beat annotations
beat_annotations = {
    'N': 'Normal beat',
    'L': 'Left bundle branch block beat',
    'R': 'Right bundle branch block beat',
    'B': 'Bundle branch block beat (unspecified)',
    'A': 'Atrial premature beat',
    'a': 'Aberrated atrial premature beat',
    'J': 'Nodal (junctional) premature beat',
    'S': 'Supraventricular premature or ectopic beat (atrial or nodal)',
    'V': 'Premature ventricular contraction',
    'r': 'R-on-T premature ventricular contraction',
    'F': 'Fusion of ventricular and normal beat',
    'e': 'Atrial escape beat',
    'j': 'Nodal (junctional) escape beat',
    'n': 'Supraventricular escape beat (atrial or nodal)',
    'E': 'Ventricular escape beat',
    '/': 'Paced beat',
    'f': 'Fusion of paced and normal beat',
    'Q': 'Unclassifiable beat',
    '?': 'Beat not classified during learning'
}

# Non-beat annotations
non_beat_annotations = {
    '[': 'Start of ventricular flutter/fibrillation',
    '!': 'Ventricular flutter wave',
    ']': 'End of ventricular flutter/fibrillation',
    'x': 'Non-conducted P-wave (blocked APC)',
    '(': 'Waveform onset',
    ')': 'Waveform end',
    'p': 'Peak of P-wave',
    't': 'Peak of T-wave',
    'u': 'Peak of U-wave',
    '`': 'PQ junction',
    '\'': 'J-point',
    '^': '(Non-captured) pacemaker artifact',
    '|': 'Isolated QRS-like artifact',
    '~': 'Change in signal quality',
    '+': 'Rhythm change',
    's': 'ST segment change',
    'T': 'T-wave change',
    '*': 'Systole',
    'D': 'Diastole',
    '=': 'Measurement annotation',
    '"': 'Comment annotation',
    '@': 'Link to external data'
}

# Combine both dictionaries
annotations = {**beat_annotations, **non_beat_annotations}