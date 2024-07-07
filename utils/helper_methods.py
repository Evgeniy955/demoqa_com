def test_number(*markers):
    def decorator(func):
        if not hasattr(func, 'markers'):
            func.markers = set()
        func.markers.update(markers)
        return func
    return decorator
