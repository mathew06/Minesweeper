from timer import Timer

# create a global Timer object
timer = None

def initialize_timer(root, label):
    global timer
    if timer is None:
        timer = Timer(root, label)
# to export timer object
def get_timer():
    return timer
