name = "nuke"

version = "17.0.4"

authors = [
    "Foundry"
]

description = \
    """
    Experience industry-standard compositing and powerful review workflows.
    """

requires = [
    ".ocio-2.4.2",
]

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
    env.PATH.prepend(f"C:\\PROGRA~1\\Nuke{version.major}.{version.minor}v{version.patch}")
    alias("nuke", f"Nuke{version.major}.{version.minor}")
    alias("nukex", f"Nuke{version.major}.{version.minor} --nukex")
    alias("nukestudio", f"Nuke{version.major}.{version.minor} --studio")
    alias("hiero", f"Nuke{version.major}.{version.minor} --hiero")
    alias("hieroplayer", f"Nuke{version.major}.{version.minor} --player")