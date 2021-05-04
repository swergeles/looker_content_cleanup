import looker_sdk
from looker_sdk import models

config_file = "looker.ini"
sdk = looker_sdk.init31(config_file)

def restore_soft_delete_dashboard(dashboard_id):
    dashboard = models.WriteDashboard(deleted=False)
    try:
        sdk.update_dashboard(str(dashboard_id), body=dashboard)
        print(f"Successfully restored dashboard {dashboard_id}")
    except Exception as e:
        print(f"Error: {e}")

def restore_soft_delete_look(look_id):
    look = models.WriteLookWithQuery(deleted=False)
    try:
        sdk.update_look(str(look_id), body=look)
        print(f"Successfully restored look {look_id}")
    except Exception as e:
        print(f"Error: {e}")

# Provide a list of look_ids to restore
looks_to_restore = []

for look in looks_to_restore:
    restore_soft_delete_look(look)

# Provide a list of dashboard_ids to restore
dashboards_to_restore = [1]

for dashboard in dashboards_to_restore:
    restore_soft_delete_dashboard(dashboard)



