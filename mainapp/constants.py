NORMAL = 0
ACCIDENT = 1
ON_FIRE = 2

FAST = 0
SLOW = 1
VERY_SLOW = 2

STATUS_CHOICES = (
  (NORMAL, "Normal"),
  (ACCIDENT, "Accident"),
  (ON_FIRE, "On Fire",),
)
STATUS_ICON_COLORS = ['green.png', 'accident.png', 'onfire.png']
SPEED_ICON_COLORS = ['green-dot.png', 'yellow-dot.png', 'red-dot.png']