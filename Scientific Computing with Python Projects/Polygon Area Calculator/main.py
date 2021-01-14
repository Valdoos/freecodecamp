# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10, 15)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(5)
print(sq.get_picture())
print(sq)

print(rect.get_amount_inside(sq))

# Run unit tests automatically
main(module='test_module', exit=False)
