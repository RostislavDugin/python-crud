from fastapi import FastAPI
from fastapi.routing import APIRoute

from ping import router as ping_router
from users import router as users_router

app = FastAPI()
app.include_router(ping_router.router)

# Print all routes to the terminal
print('API endpoints list:')
for route in app.routes:
    if isinstance(route, APIRoute):
        print(route.path)
