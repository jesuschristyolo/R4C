from robots.models import Robot


class RobotService:
    @staticmethod
    def create_robot(model, version, created):

        existing_robot = Robot.objects.filter(model=model, version=version).first()

        if not existing_robot:
            raise ValueError(f"Робот с моделью {model} и версией {version} не найден.")

        new_serial = existing_robot.serial

        robot = Robot.objects.create(
            serial=new_serial,
            model=model,
            version=version,
            created=created
        )

        return robot
