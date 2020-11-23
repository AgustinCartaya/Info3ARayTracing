class Scene:
    """Scene has all the information needed for the ray tracing engine"""

    def __init__(self, camera, objects, lights):
        self.camera = camera
        self.objects = objects
        self.lights = lights
