import sys
import os

# Add vendor to path to allow importing vendored modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vendor'))

try:
    from child_module_a import module_a
    print(module_a.hello_from_a())
except ImportError as e:
    print(f"Failed to import child_module_a: {e}")

try:
    from child_module_b import module_b
    print(module_b.hello_from_b())
except ImportError as e:
    print(f"Failed to import child_module_b: {e}")
