from solara import *

@solara.component
def MyHome():
    myparam = "kids-youtube"
    with Column():
        Title("Homepage")
    with Card():
        Markdown("#Home page")
        # AND CREATE NAVIGATE TO PAGE DETAILS
        # AND SEND PARAMETERS
        with Link(f"/details/{myparam}"):
            Button("go to details",color="primary")

# AND I CREATE PAGE AGAIN FOR GET PARAMS

@solara.component
def Details(param : str = "---"):
    router = solara.use_router()
    level = solara.use_route_level()
    # AND GET VALUE PARAMS
    youparam = router.parts[level:]
    print(youparam)

    with Column():
        Title("Details: " + router.path)
    with Card():
        Markdown("#this details page ,you params is " + "  "+ param )

# AND NOW DEFINE URL AND YOU COPONENT FOR VIEW
# NAMES MUST routes
routes = [
    Route(path="/",component=MyHome),
    Route(path="details",component=Details),
    
]
