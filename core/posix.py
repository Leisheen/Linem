#import sys
#import termios
#import tty


# -- STDOUT --
def set_ansi(self):
    """Save terminal settings and switch to raw (cbreak) mode."""
    #self.fd = sys.stdin.fileno()
    #self.old_settings = termios.tcgetattr(self.fd)
    #tty.setcbreak(self.fd)

    return self


# -- STDIN --
def restore_terminal(self):
    """Restore Linux/macOS terminal settings."""
    #termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

 
def getkey(timeout):
    # POSIX non-blocking read using select
    # Must be converted to int
    """dr, _, _ = select.select([sys.stdin], [], [], timeout)
    if dr:
        ch = sys.stdin.read(1)
        # Handle ANSI escape sequences for arrows (e.g., \x1b[A)
        if ch == '\x1b':
            dr2, _, _ = select.select([sys.stdin], [], [], 0.01)
            if dr2:
                seq = sys.stdin.read(2)
                if seq == '[A': return 'UP'
                if seq == '[B': return 'DOWN'
                if seq == '[C': return 'RIGHT'
                if seq == '[D': return 'LEFT'
        return ch"""
    return None