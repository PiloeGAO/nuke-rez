name = "nuke"

version = "16.0.1"

authors = [
    "Foundry"
]

description = \
    """
    Experience industry-standard compositing and powerful review workflows.
    """

tools = [
    "nuke",
    "nukex",
    "nukestudio",
    "hiero",
    "hieroplayer",
]

uuid = "foundry.nuke"

build_command = ""

def commands():
    alias("nuke", "C:\\PROGRA~1\\Nuke16.0v1\\Nuke16.0.exe")
    alias("nukex", "C:\\PROGRA~1\\Nuke16.0v1\\Nuke16.0.exe --nukex")
    alias("nukestudio", "C:\\PROGRA~1\\Nuke16.0v1\\Nuke16.0.exe  --studio")
    alias("hiero", "C:\\PROGRA~1\\Nuke16.0v1\\Nuke16.0.exe  --hiero")
    alias("hieroplayer", "C:\\PROGRA~1\\Nuke16.0v1\\Nuke16.0.exe  --player")