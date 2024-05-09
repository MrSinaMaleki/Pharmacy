from core.state import Auth
from core.router import Route, Router, Callback
from models import Role
router = Router(
    Route("Main", description="Maktab 112 - Pharmacy Management", children=[
        Route(
            "Login",
            condition=lambda: Auth.login_status is False,
            callback=Callback('admin.callbacks', 'login')
        ),
        Route(
            "Register",
            condition=lambda: Auth.login_status is False,
            callback=Callback('admin.callbacks', 'register')
        ),
        Route(
            "Logout",
            condition=lambda: Auth.login_status,
            callback=Callback('admin.callbacks', 'logout')
        ),
        Route("Panel",
              condition=lambda: Auth.login_status,
              children=[

                Route(
                    "List of Drugs", 
                    condition=lambda: Auth.login_status and True,
                    callback=Callback('pharmacy.callback', 'list_drug'),),

                Route("Add Drug haha!",
                    condition=lambda: Auth.login_status and Auth.check_permission(Role.Admin),
                    callback=Callback('pharmacy.callback', 'add_drug'))

              ]
        )
    ])
)
