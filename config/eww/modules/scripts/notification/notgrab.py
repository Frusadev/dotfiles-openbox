import dbus

# Connect to the session bus where Dunst notifications are sent
bus = dbus.SessionBus()
obj = bus.get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
interface = dbus.Interface(obj, "org.freedesktop.Notifications")

# Get notifications (Replace the number with how many notifications you want to fetch)
notifications = interface.GetNotifications()

# Extract data from each notification
for notification_id, notification in notifications:
    title = notification[0]  
    body = notification[2] 
    icon_name = notification[4]  # Might need adjustments based on Dunst settings 
    actions = notification[5]  # List of possible actions 

    # Example: Print neatly 
    print(f"Title: {title}")
    print(f"Body: {body}")
    print(f"Icon: {icon_name}")
    print(f"Actions: {actions}")
    print("-" * 20)  # Separator between notifications
