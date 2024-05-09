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
                    callback=Callback('funcs.callback', 'list_drug'),),

                Route("Add Drugs",
                    condition=lambda: Auth.login_status and Auth.check_permission(Role.Staff),
                    callback=Callback('funcs.callback', 'add_drug')),

                Route("Prescript Drugs",
                    condition=lambda: Auth.login_status and Auth.check_permission(Role.Doctor),
                    callback=Callback('funcs.callback', 'add_drug')),

                Route("Take drugs",
                    condition=lambda: Auth.login_status and Auth.check_permission(Role.Patient),
                    callback=Callback('funcs.callback', 'add_drug')),


              ]
        )
    ])
)
