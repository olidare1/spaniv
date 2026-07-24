from datetime import datetime, timezone, timedelta

created_at = datetime.now(timezone.utc) 
expiry_time = created_at + timedelta(minutes=7)  # Set expiry time to 7 days from creation

print("Created at:", created_at)
print("Expiry time:", expiry_time)  

