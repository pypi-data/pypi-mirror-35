from app import create_subject

next, subscribe, filter = create_subject()

def foo(msg):
    print('foo msg', msg)

def bar(msg):
    print('bar msg', msg)

def foo_two(msg):
    print('foo_two msg', msg)

foo_subscription = subscribe(foo)
bar_subscription = subscribe(bar)
print('----------------')
print('foo_subscription', foo_subscription)
next_msg('First hello')
print ('foo_nsubscribing', foo_subscription['unsubscribe']())

filtered = filter(lambda msg: True)
print('filtered', filtered)
subscription = filtered['subscribe'](foo_two)
print('filter subscription', subscription)
subscription['unsubscribe']()

next('Second hello')
