from routes import (
    wallet, 
    refferal, 
    subscribe, 
    stats,
    snapshot
    )

command_routers = [
    stats.router,
    snapshot.router
]