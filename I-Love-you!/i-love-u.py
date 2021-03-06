import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
from codebug_tether.sprites import Sprite
from codebug_tether.sprites import StringSprite

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_DIGITAL_INPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);

def build_sprite(rows):
  s = Sprite(5, 5)
  for i in range(5):
    s.set_row(i, rows[i])
  return s


codebug.scroll_sprite(build_sprite([0b00100,0b01110,0b11111,0b11111,0b11011]), 100/1000, 'L')
codebug.scroll_sprite(build_sprite([0b00100,0b01110,0b11111,0b11111,0b11011]), 100/1000, 'L')
codebug.scroll_sprite(build_sprite([0b00100,0b01110,0b11111,0b11111,0b11011]), 100/1000, 'L')
codebug.scroll_sprite(StringSprite('I LOVE YOU!!!', 'R'), 100/1000, 'L')
codebug.scroll_sprite(build_sprite([0b00100,0b01110,0b11111,0b11111,0b11011]), 100/1000, 'L')
codebug.scroll_sprite(build_sprite([0b00100,0b01110,0b11111,0b11111,0b11011]), 100/1000, 'L')
codebug.scroll_sprite(build_sprite([0b00100,0b01110,0b11111,0b11111,0b11011]), 100/1000, 'L')
