def create_subject():

    subscriptionsNext = []

    def next(msg):
        nonlocal subscriptionsNext
        [ cb(msg) for cb in subscriptionsNext ]

    # Truthy is an expression that evalutes to true or false
    def filter(truthy):
        def subscribe(next):
            nonlocal subscriptionsNext
            truthyNext = lambda msg: next(msg) if truthy(msg) else None
            subscriptionsNext.append(next)
            def unsubscribe():
                nonlocal subscriptionsNext, next
                subscriptionsNext.remove(next) if next else None
            return {
                'unsubscribe': unsubscribe
            }
        return {
            'subscribe': subscribe
        }

    
    # next should both be function
    def subscribe(next):
        nonlocal subscriptionsNext
        subscriptionsNext.append(next) if next else None
        def unsubscribe():
            nonlocal subscriptionsNext, next
            subscriptionsNext.remove(next) if next else None
        return {
            'unsubscribe': unsubscribe
        }

    return next, subscribe, filter