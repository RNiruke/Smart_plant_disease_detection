def get_severity(confidence, is_healthy=False):
    if is_healthy:
        return 'Healthy'
    if confidence < 60:
        return 'Low'
    elif confidence <= 85:
        return 'Medium'
    else:
        return 'Severe'

def get_severity_color(severity):
    return {
        'Healthy': 'success',
        'Low': 'warning',
        'Medium': 'orange',
        'Severe': 'danger',
    }.get(severity, 'secondary')

def get_severity_icon(severity):
    return {
        'Healthy': 'bi-check-circle-fill',
        'Low': 'bi-exclamation-circle',
        'Medium': 'bi-exclamation-triangle-fill',
        'Severe': 'bi-x-octagon-fill',
    }.get(severity, 'bi-question-circle')
